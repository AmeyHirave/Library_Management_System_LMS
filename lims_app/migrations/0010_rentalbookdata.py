# Generated by Django 5.0.2 on 2024-03-07 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0009_returnbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='rentalBookData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_app.booksdata')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_app.reader')),
            ],
        ),
    ]
