# Generated by Django 2.1.3 on 2019-05-16 12:41

from django.db import migrations, models
import django_db_cascade.deletions
import django_db_cascade.fields


def link_diseases(apps, schema_editor):
    # using the string in 'disease', associate samples and curation entries to the corresponding Disease model
    Disease = apps.get_model('api', 'Disease')
    Sample = apps.get_model('api', 'Sample')
    CurationEntry = apps.get_model('api', 'CurationEntry')

    for sample in Sample.objects.all():
        sample.disease_link = Disease.objects.get(svip_variant=sample.svip_variant, name=sample.disease)
        sample.save()

    for curation in CurationEntry.objects.all():
        try:
            curation.disease_link = Disease.objects.get(svip_variant=curation.svip_variant, name=curation.disease)
            curation.save()
        except Exception as ex:
            print("Failed to link %s to disease %s w/svip var w/diseases %s" % (
                curation.id, curation.disease, curation.svip_variant.data['diseases']
            ))
            raise ex


def unlink_diseases(apps, schema_editor):
    # restore the disease field to being a string a containing the disease's name
    Sample = apps.get_model('api', 'Sample')
    CurationEntry = apps.get_model('api', 'CurationEntry')

    for sample in Sample.objects.all():
        sample.disease = sample.disease_link.name
        sample.save()

    for curation in CurationEntry.objects.all():
        curation.disease = curation.disease_link.name
        curation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20190516_0929'),
    ]

    operations = [

        # 1b. perform association to new disease_link field
        migrations.RunPython(code=link_diseases, reverse_code=unlink_diseases),

        # 2. remove the now unnecessary disease field...
        migrations.RemoveField(
            model_name='curationentry',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='disease',
        ),

        # 3. ...and swap the new linked field in for the old, removed field
        migrations.RenameField(
            model_name='curationentry',
            old_name='disease_link',
            new_name='disease'
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='disease_link',
            new_name='disease'
        ),

        # 4. also make the field non-nullable now that we've associated everything
        migrations.AlterField(
            model_name='curationentry',
            name='disease',
            field=django_db_cascade.fields.ForeignKey(
                on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.Disease', null=False)
        ),
        migrations.AlterField(
            model_name='sample',
            name='disease',
            field=django_db_cascade.fields.ForeignKey(
                on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.Disease', null=False)
        ),

        # break the direct associations to VariantInSVIP now that we can indirectly access it via Disease
        migrations.RemoveField(
            model_name='curationentry',
            name='svip_variant',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='svip_variant',
        )
    ]