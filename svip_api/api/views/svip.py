import django_filters
from django.http import JsonResponse
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

from api.models import (
    VariantInSVIP, Sample,
    DiseaseInSVIP,
    CurationEntry
)
from api.permissions import IsCurationPermitted
from api.serializers import (
    VariantInSVIPSerializer, SampleSerializer
)
from api.serializers.svip import CurationEntrySerializer, DiseaseInSVIPSerializer


class VariantInSVIPViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Connects a variant, e.g. EGFR L858R, to its SVIP-specific data. Currently that consists of samples
    and curation data, but more will come in the future.
    """
    serializer_class = VariantInSVIPSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if 'variant_pk' in self.kwargs:
            q = VariantInSVIP.objects.filter(variant_id=self.kwargs['variant_pk'])
        else:
            q = VariantInSVIP.objects.all().prefetch_related('diseaseinsvip_set', 'diseaseinsvip_set__sample_set')

        return q

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = (
        'variant__gene',
        'variant__gene__symbol',
        'variant__name'
    )

    search_fields = (
        'variant__gene__symbol',
        'variant__name',
        'disease__name'
    )


class DiseaseInSVIPViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Connects a variant, e.g. EGFR L858R, to its SVIP-specific data. Currently that consists of samples
    and curation data, but more will come in the future.
    """
    serializer_class = DiseaseInSVIPSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        if 'svip_variant_pk' in self.kwargs:
            q = DiseaseInSVIP.objects.filter(svip_variant_id=self.kwargs['svip_variant_pk'])
        else:
            q = DiseaseInSVIP.objects.all()
        return q


class IsSampleViewer(permissions.BasePermission):
    """
    Allows only individuals with the view_sample permission to view samples.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('api.view_sample')


class SampleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SampleSerializer
    permission_classes = (permissions.IsAuthenticated, IsSampleViewer)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = (
        'disease_in_svip__disease', 'sample_id', 'year_of_birth', 'gender', 'hospital', 'medical_service', 'provider_annotation',
        'sample_tissue', 'tumor_purity', 'tnm_stage', 'sample_type', 'sample_site', 'specimen_type', 'sequencing_date',
        'panel', 'coverage', 'calling_strategy', 'caller', 'aligner', 'software', 'software_version', 'platform',
        'contact',
    )
    ordering_fields = filter_fields
    search_fields = filter_fields

    def get_queryset(self):
        if not self.request.user.has_perm('api.view_sample'):
            raise PermissionDenied(detail="You do not have the necessary permissions to view sample data")

        if 'disease_pk' in self.kwargs and 'variant_in_svip_pk' in self.kwargs:
            q = Sample.objects.filter(
                disease_in_svip_id=self.kwargs['disease_pk'],
                disease_in_svip__svip_variant_id=self.kwargs['variant_in_svip_pk']
            )
        else:
            q = Sample.objects.all()

        return q.order_by('id')


class CurationEntryViewSet(viewsets.ModelViewSet):
    """
    Curation entry for a specific variant w/SVIP data and disease.
    """
    serializer_class = CurationEntrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurationPermitted)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = (
        'owner',
        'disease',
        'variants'
    )
    ordering_fields = '__all__'
    search_fields = (
        'annotations',
        'comment',
        'drug',
        'effect',
        'mutation_origin',
        'references',
        'status',
        'summary',
        'support',
        'tier_level',
        'tier_level_criteria',
        'type_of_evidence',
    )

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=True)
    def history(self, request, pk):
        entry = CurationEntry.objects.get(id=pk)
        history = list(entry.history.all())
        deltas = (
            {'time': a.history_date, 'diff': a.diff_against(b)}
            for a, b in zip(history[:-1], history[1:])
        )

        return JsonResponse({
            'created_on': history[0].history_date if len(history) > 0 else None,
            'deltas': [
                {
                    'time': str(delta['time']),
                    'changes': [
                        {
                            'field': change.field,
                            'old': change.old,
                            'new': change.new
                        }
                        for change in delta['diff'].changes
                    ]
                }
                for delta in deltas
            ]
        })

    def get_queryset(self):
        user = self.request.user
        result = None

        if user.is_authenticated:
            if user.is_superuser:
                # superusers can see everything
                result = CurationEntry.objects.all()
            if user.groups.filter(name='curators').exists():
                # curators see only their own entries
                result = CurationEntry.objects.filter(owner=user)
            elif user.groups.filter(name='reviewers').exists():
                # FIXME: should reviewers see all entries, or just the ones they've been assigned?
                result = CurationEntry.objects.filter(status__in=('reviewed', 'submitted'))

        if not result:
            # unauthenticated users and other users who don't have specific roles just see the default set
            result = CurationEntry.objects.filter(status='reviewed')

        # pre-select variant and gene data to prevent thousands of queries
        result = (
            result
                .select_related('owner')
                .prefetch_related('variants', 'disease')
        )

        return result.order_by('created_on')
