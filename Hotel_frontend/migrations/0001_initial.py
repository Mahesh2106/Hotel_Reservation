# Generated by Django 3.2.10 on 2023-08-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=600, null=True)),
                ('Password', models.CharField(blank=True, max_length=600, null=True)),
                ('Email', models.EmailField(blank=True, max_length=400, null=True)),
                ('Phone_number', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
    ]
