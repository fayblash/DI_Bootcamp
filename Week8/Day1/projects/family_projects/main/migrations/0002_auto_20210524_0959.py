# Generated by Django 3.2.3 on 2021-05-24 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='person',
            name='has_pet',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='number_pet',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
