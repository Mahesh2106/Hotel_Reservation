# Generated by Django 3.2.10 on 2023-07-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_rooms',
            name='Room_Number',
        ),
        migrations.AddField(
            model_name='hotel_rooms',
            name='Room_price',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
