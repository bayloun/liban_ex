# Generated by Django 2.0 on 2018-02-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180219_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.TextField(max_length=100),
        ),
    ]