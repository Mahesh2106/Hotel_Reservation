# Generated by Django 3.2.10 on 2023-08-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0023_auto_20230819_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_And_Beverages',
            fields=[
                ('Item_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Item_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Item_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Item_Price', models.IntegerField(blank=True, null=True)),
                ('Item_Image', models.ImageField(blank=True, null=True, upload_to='Frontend Beverages Section')),
            ],
        ),
    ]
