# Generated by Django 3.2.10 on 2023-08-09 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0011_hotel_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='Image1',
        ),
        migrations.RemoveField(
            model_name='features',
            name='Image2',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Image1',
        ),
    ]
