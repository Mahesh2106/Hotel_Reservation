# Generated by Django 3.2.10 on 2023-08-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]
