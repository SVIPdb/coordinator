# Generated by Django 2.1.3 on 2018-11-29 14:18

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20181128_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('drug_labels', models.CharField(max_length=120, null=True)),
                ('variant_name', models.TextField(null=True)),
                ('source_link', models.TextField(null=True)),
                ('evidence_label', models.CharField(max_length=20, null=True)),
                ('response_type', models.CharField(max_length=20, null=True)),
                ('evidence_level', models.CharField(max_length=20, null=True)),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Gene')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentalContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=120)),
                ('term', models.CharField(max_length=120)),
                ('envcontext_id', models.CharField(max_length=120)),
                ('usan_stem', models.CharField(max_length=120)),
                ('description', models.TextField(null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('predictive', 'Predictive'), ('prognostic', 'Prognostic'), ('predisposing', 'Predisposing'), ('diagnostic', 'Diagnostic')], max_length=20)),
                ('description', models.TextField(null=True)),
                ('publications', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Publication URLs')),
                ('evidenceType_sourceName', models.CharField(max_length=120, null=True)),
                ('evidenceType_id', models.CharField(max_length=120, null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Phenotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=120, null=True)),
                ('term', models.CharField(max_length=120, null=True)),
                ('pheno_id', models.CharField(max_length=120, null=True)),
                ('family', models.CharField(max_length=120, null=True)),
                ('description', models.TextField(null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Association')),
            ],
        ),
    ]
