# Generated by Django 3.2.10 on 2023-09-11 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0034_auto_20230911_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 9, 30, 11, 319741)),
        ),
    ]
