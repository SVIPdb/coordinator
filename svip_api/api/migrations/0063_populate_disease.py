# Generated by Django 2.2.4 on 2019-10-23 12:08
import os
from csv import DictReader

from django.db import migrations, transaction


def create_diseases(apps, schema_editor):
    # for now, we're going to fake the disease table by populating it from our mock SVIP variants
    Disease = apps.get_model('api', 'Disease')
    DiseaseInSVIP = apps.get_model('api', 'DiseaseInSVIP')

    # we also need DiseaseInSVIP to point to these newly-created diseases
    for entry in DiseaseInSVIP.objects.all():
        (item, created) = Disease.objects.get_or_create(name=entry.name, defaults={
            'name': entry.name,
            'icdo_code': None
        })
        entry.disease = item
        entry.save()


def drop_diseases(apps, schema_editor):
    Disease = apps.get_model('api', 'Disease')
    Disease.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_create_disease'),
    ]

    operations = [
        migrations.RunPython(create_diseases, reverse_code=drop_diseases)
    ]
