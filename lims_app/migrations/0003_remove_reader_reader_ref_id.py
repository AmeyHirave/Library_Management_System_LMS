# Generated by Django 5.0.2 on 2024-02-27 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0002_rename_reference_id_reader_reader_ref_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='reader_ref_id',
        ),
    ]
