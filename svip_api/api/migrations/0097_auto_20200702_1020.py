# Generated by Django 2.2.4 on 2020-07-02 10:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0096_fix_collapsed_missing_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvariantinsvip',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='variantinsvip',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
