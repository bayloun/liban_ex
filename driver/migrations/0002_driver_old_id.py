# Generated by Django 2.0 on 2018-02-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='old_id',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
