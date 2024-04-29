# Generated by Django 4.2 on 2024-04-29 02:59

import cloudinary.models
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbl_category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='api.category')),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
    ]
