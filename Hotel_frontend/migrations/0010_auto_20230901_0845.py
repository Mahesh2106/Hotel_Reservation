# Generated by Django 3.2.10 on 2023-09-01 03:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0024_food_and_beverages'),
        ('Hotel_frontend', '0009_auto_20230831_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 8, 45, 3, 957615)),
        ),
        migrations.CreateModel(
            name='Beverages_Booking',
            fields=[
                ('Booking_Beverages_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Item_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Session', models.CharField(blank=True, max_length=100, null=True)),
                ('Selected_date', models.DateField()),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
                ('Item_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_admin.food_and_beverages')),
                ('Room_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_admin.room')),
            ],
        ),
    ]