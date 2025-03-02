# Generated by Django 5.1.6 on 2025-02-11 06:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_customer_created_at_customer_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='orderline',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
