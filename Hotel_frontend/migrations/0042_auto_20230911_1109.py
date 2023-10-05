# Generated by Django 3.2.10 on 2023-09-11 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0041_auto_20230911_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 11, 9, 49, 276427)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Check_Out_Time',
            field=models.TimeField(blank=True, null=True, verbose_name='Out Time'),
        ),
    ]