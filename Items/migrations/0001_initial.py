# Generated by Django 4.2.4 on 2023-08-27 14:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(1)])),
                ('image', models.ImageField(blank=True, default='items/stand-in-photos/stand-in-items.jpeg', upload_to='uploads/items/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.category')),
            ],
        ),
    ]
