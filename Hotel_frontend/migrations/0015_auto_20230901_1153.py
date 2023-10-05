# Generated by Django 3.2.10 on 2023-09-01 06:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0024_food_and_beverages'),
        ('Hotel_frontend', '0014_auto_20230901_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverages_booking',
            name='Room_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel_admin.room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 11, 53, 10, 149246)),
        ),
    ]