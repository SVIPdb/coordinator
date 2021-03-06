# Generated by Django 2.2.4 on 2019-11-18 10:03

from django.db import migrations, models
import django.db.models.deletion
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0080_auto_20191118_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curationentry',
            name='variant',
            field=models.ForeignKey(null=False, on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.Variant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalcurationentry',
            name='variant',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.Variant'),
        ),
    ]
