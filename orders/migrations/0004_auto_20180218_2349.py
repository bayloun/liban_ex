# Generated by Django 2.0 on 2018-02-18 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180218_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['order_id']},
        ),
    ]
