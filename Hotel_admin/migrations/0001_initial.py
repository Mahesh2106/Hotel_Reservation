# Generated by Django 3.2.10 on 2023-07-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_Number', models.IntegerField(blank=True, null=True)),
                ('Room_Image', models.ImageField(blank=True, null=True, upload_to='Room Images')),
                ('Room_Category', models.CharField(blank=True, max_length=1800, null=True)),
                ('Room_Description', models.CharField(blank=True, max_length=1500, null=True)),
            ],
        ),
    ]
