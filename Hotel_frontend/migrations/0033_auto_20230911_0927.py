# Generated by Django 3.2.10 on 2023-09-11 03:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0032_delete_customer_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 9, 27, 35, 316583)),
        ),
        migrations.CreateModel(
            name='PaymentDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardHolder_Name', models.CharField(blank=True, max_length=900, null=True)),
                ('Card_Num', models.CharField(blank=True, max_length=50, null=True)),
                ('Amount', models.CharField(blank=True, max_length=900, null=True)),
                ('Expiry_Date', models.CharField(blank=True, max_length=50, null=True)),
                ('CVV', models.CharField(blank=True, max_length=10, null=True)),
                ('Cust_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_frontend.registration')),
            ],
        ),
    ]