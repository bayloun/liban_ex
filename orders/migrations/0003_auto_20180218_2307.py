# Generated by Django 2.0 on 2018-02-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180218_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='actual_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
