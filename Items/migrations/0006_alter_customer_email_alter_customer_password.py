# Generated by Django 4.2.4 on 2023-08-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0005_alter_customer_display_name_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
