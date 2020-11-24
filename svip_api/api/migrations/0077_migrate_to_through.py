# Generated by Django 2.2.4 on 2019-11-15 12:29

from django.db import migrations


# noinspection SqlWithoutWhere
class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_auto_20191115_1229'),
    ]

    operations = [
        migrations.RunSQL(
            """
            insert into svip_variantcuration (curationentry_id, variant_id)
            select curationentry_id, variant_id from svip_curationentry_variants
            """,
            reverse_sql="""
            delete from svip_variantcuration
            """
        )
    ]
