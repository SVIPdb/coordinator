# Generated by Django 2.1.3 on 2019-01-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190116_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='alt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='ref',
            field=models.TextField(null=True),
        ),
    ]
