# Generated by Django 2.1.3 on 2019-03-08 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20190306_0758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='association',
            old_name='response_type',
            new_name='clinical_significance',
        ),
    ]
