# Generated by Django 3.2.10 on 2023-09-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0030_delete_customer_pay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardHolder_Name', models.CharField(blank=True, max_length=900, null=True)),
                ('Card_Num', models.CharField(blank=True, max_length=50, null=True)),
                ('Amount', models.CharField(blank=True, max_length=900, null=True)),
                ('Expiry_Date', models.CharField(blank=True, max_length=50, null=True)),
                ('CVV', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
