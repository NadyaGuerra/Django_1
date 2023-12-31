# Generated by Django 4.2.3 on 2023-07-14 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наиминование')),
                ('description', models.TextField(verbose_name='описание')),
                ('preview', models.ImageField(upload_to='products/', verbose_name='изображение')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price', models.DecimalField(decimal_places=10, max_digits=10, verbose_name='цена')),
                ('created_data', models.DateTimeField(default=datetime.datetime.now, verbose_name='дата создания')),
                ('last_change', models.DateTimeField(default=datetime.datetime.now, verbose_name='последние изменения')),
            ],
        ),
    ]
