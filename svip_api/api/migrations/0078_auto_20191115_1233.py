# Generated by Django 2.2.4 on 2019-11-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_migrate_to_through'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curationentry',
            name='variants'
        ),
        migrations.RenameField(
            model_name='curationentry',
            old_name='variants_new',
            new_name='variants'
        )
    ]
