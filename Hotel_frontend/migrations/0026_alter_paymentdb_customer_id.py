# Generated by Django 3.2.10 on 2023-09-11 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0025_auto_20230911_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdb',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_frontend.registration'),
        ),
    ]