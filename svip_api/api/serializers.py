from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from api.models import Source, Gene, Variant, Association, Phenotype, Evidence, EnvironmentalContext, VariantInSource


# -----------------------------------------------------------------------------
# --- app management serializers
# -----------------------------------------------------------------------------

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# -----------------------------------------------------------------------------
# --- top-level genomic entities, e.g. genes, variants
# -----------------------------------------------------------------------------

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = (
            'url',
            'name',
            'display_name',
            'num_variants',
        )


class GeneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gene
        fields = '__all__'


class VariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variant
        # fields = (
        #     'url',
        #     'gene',
        #     'name',
        #     'description',
        #     'biomarker_type',
        #     'so_hierarchy',
        #     'soid',
        #     'so_name',
        #     'sources',
        #     'association_set'
        # )

        fields = [field.name for field in model._meta.fields]
        fields.append('url')
        fields.append('gene')
        fields.append('gene_symbol')
        fields.remove('mv_info')  # redacted in the list view because it's too verbose

        # FIXME: add sources collection here, from VariantInSource


class VariantInSourceSerializer(serializers.HyperlinkedModelSerializer):
    variant = serializers.HyperlinkedRelatedField('variant-detail', read_only=True)
    source = SourceSerializer()
    # association_set = serializers.HyperlinkedRelatedField('association-detail', read_only=True, many=True)
    # association_set = AssociationSerializer(many=True, read_only=True)

    associations_url = serializers.SerializerMethodField()

    def get_associations_url(self, obj):
        # FIXME: ideally, this should link by reference to the associations nested router, but we're hardcoding it here
        #  because i can't figure out how to do that :\
        our_url = reverse('variantinsource-detail', args=[obj.id], request=self.context['request'])
        return "%s/associations" % our_url

    class Meta:
        model = VariantInSource
        fields = (
            'url',
            'variant',
            'source',
            'variant_url',
            'extras',
            'associations_url',
            'association_count',
            'publication_count',
            'clinical_significances',
            'evidence_types',
            'diseases',
            'contexts',
            'scores',
            # 'association_set'
        )
        # depth = 1


class FullVariantSerializer(VariantSerializer):
    # sources_set = VariantInSourceSerializer(many=True)
    variantinsource_set = VariantInSourceSerializer(many=True, read_only=True)

    def __init__(self, *args, **kwargs):
        super(FullVariantSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Variant
        depth = 1
        fields = VariantSerializer.Meta.fields.copy()
        fields.append('mv_info')
        fields.append('variantinsource_set')
        fields.append('svip_data')


# -----------------------------------------------------------------------------
# --- variant evidence entries
# -----------------------------------------------------------------------------

class AssociationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Association
        depth = 1
        fields = (
            'url',
            # 'gene',
            # 'variant',
            'source_url',
            'source',
            'description',
            'drug_labels',
            'variant_name',
            'source_link',

            'evidence_type',
            'evidence_direction',
            'clinical_significance',
            'evidence_level',

            'phenotype_set',
            'evidence_set',
            'environmentalcontext_set'
        )


class PhenotypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phenotype
        fields = '__all__'


class EvidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'


class EnvironmentalContextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnvironmentalContext
        fields = '__all__'
