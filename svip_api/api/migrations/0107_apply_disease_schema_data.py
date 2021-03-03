# Generated by Django 2.2.4 on 2021-01-26 16:26

from django.db import connection, migrations, models

import os

def load_data_from_sql(filename):
    file_path = os.path.join(os.path.dirname(__file__), '../fixtures/', filename)
    sql_statement = open(file_path).read()
    with connection.cursor() as c:
        c.execute(sql_statement)

def change_disease_schema(apps, schema_editor):
    # first, we import the ICD-O tables (no effect on existing tables yet)
    load_data_from_sql('disease-schema-migration/dump_icd-o_tables.sql')

    # then, we modify api_disease's schema to just point to entries in the new ICD-O tables
    load_data_from_sql('disease-schema-migration/connection_to_api_disease.sql')

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0106_merge_sviptest_diseases'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(change_disease_schema, reverse_code=migrations.RunPython.noop)
            ],
            state_operations=[
                # these ops were generated by a 'makemigrations' invocation after having run 'change_disease_schema' above.
                # SeparateDatabaseAndState basically tells django's change detection system that these changes have
                # been applied by the 'database_operations' steps above, without django
                # having to apply them itself.
                migrations.CreateModel(
                    name='IcdOMorpho',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('cell_type_code', models.TextField()),
                        ('term', models.TextField()),
                        ('code_reference', models.TextField(blank=True, null=True)),
                        ('obs', models.BooleanField()),
                        ('additional_information', models.TextField(blank=True, null=True)),
                        ('created_on', models.DateTimeField(blank=True, null=True)),
                        ('user_created', models.BooleanField()),
                    ],
                    options={
                        'db_table': 'icd_o_morpho',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOMorphoBehavior',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('behavior_code', models.IntegerField()),
                        ('behavior_description', models.TextField()),
                    ],
                    options={
                        'db_table': 'icd_o_morpho_behavior',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOMorphoLevel',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('level', models.TextField()),
                        ('icd_o_level', models.BooleanField()),
                    ],
                    options={
                        'db_table': 'icd_o_morpho_level',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOMorphoVersion',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('version', models.TextField()),
                    ],
                    options={
                        'db_table': 'icd_o_morpho_version',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOTopo',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('topo_code', models.TextField(blank=True, null=True)),
                        ('topo_term', models.TextField(blank=True, null=True)),
                    ],
                    options={
                        'db_table': 'icd_o_topo',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOTopoApiDisease',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ],
                    options={
                        'db_table': 'icd_o_topo_api_disease',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOTopoLevel',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('level', models.TextField()),
                    ],
                    options={
                        'db_table': 'icd_o_topo_level',
                        'managed': False,
                    },
                ),
                migrations.CreateModel(
                    name='IcdOTopoVersion',
                    fields=[
                        ('id',
                        models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('version', models.TextField()),
                    ],
                    options={
                        'db_table': 'icd_o_topo_version',
                        'managed': False,
                    },
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='abbreviation',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='details',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='localization',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='morpho_code',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='name',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='snomed_code',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='snomed_name',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='topo_code',
                ),
                migrations.RemoveField(
                    model_name='disease',
                    name='user_created',
                ),
                migrations.AlterField(
                    model_name='disease',
                    name='created_on',
                    field=models.DateTimeField(blank=True, null=True),
                ),
                migrations.AddField(
                    model_name='disease',
                    name='icd_o_morpho',
                    field=models.ForeignKey(blank=True, null=True, on_delete=models.deletion.DO_NOTHING,
                        to='api.IcdOMorpho'),
                ),
            ]
        )

    ]