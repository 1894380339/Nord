# Generated by Django 4.0.3 on 2022-04-09 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='md_contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 14, 42, 44, 545763)),
        ),
    ]
