# Generated by Django 3.2.10 on 2023-09-11 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0027_rename_paymentdb_customer_payment'),
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
                ('Customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_frontend.registration')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer_Payment',
        ),
    ]