# Generated by Django 5.1.5 on 2025-03-01 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_partnerprofile_alternate_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerprofile',
            name='alternate_number',
        ),
    ]
