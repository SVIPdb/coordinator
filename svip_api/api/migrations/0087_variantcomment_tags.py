# Generated by Django 2.2.4 on 2020-01-10 13:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_remove_comment_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='variantcomment',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None),
        ),
    ]
