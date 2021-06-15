# Generated by Django 2.2.13 on 2021-06-15 13:22

from django.db import migrations, models
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0111_auto_20210615_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summarycomment',
            name='variant',
            field=models.ForeignKey(default=278, on_delete=django_db_cascade.deletions.DB_CASCADE, related_name='summary_comments', to='api.VariantInSVIP'),
        ),
    ]
