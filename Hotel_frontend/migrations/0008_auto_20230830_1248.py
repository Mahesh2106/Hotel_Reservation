# Generated by Django 3.2.10 on 2023-08-30 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0007_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 8, 30, 12, 48, 40, 739234)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Proof_Id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Username',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
