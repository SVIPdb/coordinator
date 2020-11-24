# Generated by Django 2.2.4 on 2019-11-18 09:35

from django.db import migrations, models
import django.db.models.deletion
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0078_auto_20191115_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curationentry',
            old_name='variants',
            new_name='extra_variants',
        ),
        migrations.AddField(
            model_name='curationentry',
            name='variant',
            field=models.ForeignKey(null=True, on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.Variant'),
            preserve_default=False,
        ),
    ]
