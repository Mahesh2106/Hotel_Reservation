# Generated by Django 3.2.10 on 2023-09-11 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0026_alter_paymentdb_customer_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentDB',
            new_name='Customer_Payment',
        ),
    ]
