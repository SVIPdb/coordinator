# Generated by Django 2.2.4 on 2019-10-24 08:03

from django.db import migrations
import django_db_cascade.deletions
import django_db_cascade.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_auto_20191024_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curationentry',
            name='disease',
            field=django_db_cascade.fields.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.Disease'),
        ),
        migrations.AlterField(
            model_name='diseaseinsvip',
            name='disease',
            field=django_db_cascade.fields.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.Disease'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='disease_in_svip',
            field=django_db_cascade.fields.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.DiseaseInSVIP'),
        ),
    ]