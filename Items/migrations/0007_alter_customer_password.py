# Generated by Django 4.2.4 on 2023-08-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0006_alter_customer_email_alter_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
