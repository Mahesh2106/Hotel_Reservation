# Generated by Django 3.2.10 on 2023-08-09 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0015_rooms_room_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='Room_category',
        ),
    ]