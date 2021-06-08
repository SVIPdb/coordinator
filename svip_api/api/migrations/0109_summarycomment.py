# Generated by Django 2.2.13 on 2021-06-08 02:55

from django.conf import settings
from django.db import migrations, models
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0108_IcdOTopoApiDisease_add_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variant', models.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, related_name='summary_comments', to='api.VariantInSVIP')),
            ],
        ),
    ]
