# Generated by Django 3.2.10 on 2023-09-01 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0011_auto_20230901_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverages_booking',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 9, 26, 2, 883941)),
        ),
    ]