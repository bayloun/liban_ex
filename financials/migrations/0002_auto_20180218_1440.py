# Generated by Django 2.0 on 2018-02-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial',
            name='order',
        ),
        migrations.AlterField(
            model_name='financial',
            name='status',
            field=models.CharField(choices=[('Undelivered', 'Undelivered'), ('Delivered with driver', 'Delivered with driver'), ('Delivered with company', 'Delivered with company'), ('Paid to seller', 'Paid to seller')], max_length=20),
        ),
    ]
