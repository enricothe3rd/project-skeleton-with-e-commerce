# Generated by Django 5.1.6 on 2025-02-11 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_order_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_code',
            field=models.CharField(editable=False, max_length=50, unique=True),
        ),
    ]
