# Generated by Django 5.1.5 on 2025-03-19 04:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collectionplans', '0001_initial'),
        ('financials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refunds', to='financials.transaction'),
        ),
        migrations.AddField(
            model_name='scheme',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_schemes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scheme',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_schemes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cashcollection',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='collectionplans.scheme'),
        ),
    ]
