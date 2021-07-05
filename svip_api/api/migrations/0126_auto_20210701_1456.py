# Generated by Django 2.2.24 on 2021-07-01 14:56

import django.contrib.postgres.fields
from django.db import migrations, models
import django_db_cascade.deletions
import django_db_cascade.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0125_merge_20210701_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='curationreview',
            name='curation_entry',
            field=django_db_cascade.fields.ForeignKey(default=520, on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.CurationEntry'),
        ),
        migrations.AlterField(
            model_name='curationentry',
            name='annotations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='historicalcurationentry',
            name='annotations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None),
        ),
    ]