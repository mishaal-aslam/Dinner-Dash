# Generated by Django 4.2.4 on 2023-08-30 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_order_status_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 30, 12, 44, 46, 517347)),
        ),
    ]
