# Generated by Django 5.1.5 on 2025-03-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='other_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
