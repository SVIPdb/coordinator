# Generated by Django 2.1.3 on 2018-11-22 14:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='so_hierarchy',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), null=True, size=None, verbose_name='Hierarchy of SO IDs'),
        ),
    ]
