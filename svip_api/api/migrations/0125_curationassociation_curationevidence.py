# Generated by Django 2.2.13 on 2021-06-22 05:40

from django.db import migrations, models
import django.db.models.deletion
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0124_auto_20210621_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurationAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Disease')),
                ('variant', models.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, related_name='curation_associations', to='api.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='CurationEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_evidence', models.TextField(default='')),
                ('association', models.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, related_name='curation_evidences', to='api.CurationAssociation')),
            ],
        ),
    ]
