# Generated by Django 3.2.10 on 2023-09-11 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0024_auto_20230910_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdb',
            name='Customer_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Hotel_frontend.registration'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Booking_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='Email',
            field=models.EmailField(blank=True, max_length=600, null=True, unique=True),
        ),
    ]
