# Generated by Django 2.0 on 2018-02-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20180218_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='beirut_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='lebanon_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]