# Generated by Django 3.2.10 on 2023-09-02 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0015_auto_20230901_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 2, 8, 42, 11, 412263)),
        ),
    ]