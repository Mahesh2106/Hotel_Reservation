# Generated by Django 3.2.10 on 2023-07-31 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_admin', '0004_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='Price',
            new_name='Price_Range',
        ),
    ]
