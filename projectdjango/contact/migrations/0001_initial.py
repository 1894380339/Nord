# Generated by Django 4.0.3 on 2022-04-09 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='md_contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
                ('content', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(default=datetime.datetime(2022, 4, 9, 14, 41, 18, 298668))),
            ],
        ),
    ]
