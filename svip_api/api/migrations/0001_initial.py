# Generated by Django 2.1.3 on 2018-11-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.BigIntegerField()),
                ('hugo_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvs_cdna', models.TextField()),
                ('gene', models.ForeignKey(on_delete='cascade', to='api.Gene')),
            ],
        ),
    ]
