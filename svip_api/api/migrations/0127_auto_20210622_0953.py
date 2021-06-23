# Generated by Django 2.2.13 on 2021-06-22 09:53

from django.db import migrations, models
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0126_auto_20210622_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curationentry',
            name='curation_evidences',
            field=models.ForeignKey(null=True, on_delete=django_db_cascade.deletions.DB_CASCADE, related_name='curation_entries', to='api.CurationEvidence'),
        ),
    ]