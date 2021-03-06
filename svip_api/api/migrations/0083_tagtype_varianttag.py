# Generated by Django 2.2.4 on 2019-12-07 12:23

from django.db import migrations, models
import django.utils.timezone
import django_db_cascade.deletions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_create_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(db_index=True)),
                ('created_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='VariantTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.VariantComment')),
                ('type', models.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE, to='api.TagType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
