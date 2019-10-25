# Generated by Django 2.2.4 on 2019-10-24 20:31
import os
from csv import DictReader

from django.db import migrations

import api

APP_DIR = os.path.dirname(api.__file__)
DISEASES_TSV = os.path.join(APP_DIR, "fixtures", "diseases.tsv")


def populate_diseases(apps, schema_editor):
    with open(DISEASES_TSV) as fp:
        Disease = apps.get_model('api', 'Disease')

        added_set = set()

        for s in DictReader(fp, dialect='excel-tab'):
            candidate = Disease(
                localization=s['localization'],
                abbreviation=s['abbreviation'],
                name=s['name'],
                topo_code=s['topo_code'],
                morpho_code=s['morpho_code'],
                snomed_code=s['snomed_code'],
                snomed_name=s['snomed_name'],
                details=s['details'],
            )
            candidate.save()

            # save these for when we delete everything that we didn't add at the end
            added_set.add(candidate.id)

    added_instances = Disease.objects.filter(id__in=added_set)

    # hook up DiseaseInSVIP and CurationEntry to the correct new diseases
    DiseaseInSVIP = apps.get_model('api', 'DiseaseInSVIP')
    CurationEntry = apps.get_model('api', 'CurationEntry')

    for model in (DiseaseInSVIP.objects.all(), CurationEntry.objects.all()):
        for entry in model:
            try:
                entry.disease = added_instances.filter(name__iexact=entry.disease.name).first()
                entry.save()
            except Exception as ex:
                print("Failed when trying to find %s" % entry.disease.name)
                raise ex

    # clear out all the non-added entries
    Disease.objects.exclude(id__in=added_set).delete()


def drop_diseases(apps, schema_editor):
    # remove anything that appears in the file
    with open(DISEASES_TSV) as fp:
        Disease = apps.get_model('api', 'Disease')

        for s in DictReader(fp, dialect='excel-tab'):
            Disease.objects.filter(
                localization=s['localization'],
                abbreviation=s['abbreviation'],
                name=s['name'],
                topo_code=s['topo_code'],
                morpho_code=s['morpho_code'],
                snomed_code=s['snomed_code'],
                snomed_name=s['snomed_name'],
                details=s['details'],
            ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_update_disease'),
    ]

    operations = [
        migrations.RunPython(populate_diseases, reverse_code=drop_diseases)
    ]
