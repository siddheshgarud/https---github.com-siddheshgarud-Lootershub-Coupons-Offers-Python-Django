# Generated by Django 3.2.4 on 2021-06-24 21:44

import Stores.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0004_storecoupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='sslug',
            field=models.CharField(default=Stores.models.randomString, max_length=25),
        ),
    ]