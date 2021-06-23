# Generated by Django 2.2.13 on 2021-06-23 13:03

from django.db import migrations
import django_db_cascade.deletions
import django_db_cascade.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0125_auto_20210623_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curationreview',
            name='curation_evidence',
            field=django_db_cascade.fields.ForeignKey(null=True, on_delete=django_db_cascade.deletions.DB_CASCADE, related_name='reviews', to='api.CurationEvidence'),
        ),
    ]
