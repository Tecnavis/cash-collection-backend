# Generated by Django 5.1.5 on 2025-03-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
    ]
