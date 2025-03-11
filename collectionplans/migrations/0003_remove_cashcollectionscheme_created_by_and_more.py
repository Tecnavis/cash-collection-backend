# Generated by Django 5.1.5 on 2025-03-11 06:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectionplans', '0002_initial'),
        ('customer', '0002_customer_other_info'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashcollectionscheme',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='cashcollectionscheme',
            name='customers',
        ),
        migrations.RemoveField(
            model_name='cashcollectionscheme',
            name='updated_by',
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('collection_frequency', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('custom', 'Custom')], max_length=10)),
                ('installment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_schemes', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_schemes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CashCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_collections', to=settings.AUTH_USER_MODEL)),
                ('customers', models.ManyToManyField(related_name='cash_collections', to='customer.customer')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_collections', to=settings.AUTH_USER_MODEL)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='collectionplans.scheme')),
            ],
        ),
    ]
