# Generated by Django 2.1.3 on 2019-01-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_variant_lowercase_name_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='ensembl_gene_id',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='symbol',
            field=models.TextField(db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='biomarker_type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='isoform',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='name',
            field=models.TextField(db_index=True, verbose_name='Variant Name'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='reference_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='refseq',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='so_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='soid',
            field=models.TextField(default='', null=True, verbose_name='Sequence Ontology ID'),
        ),
    ]
