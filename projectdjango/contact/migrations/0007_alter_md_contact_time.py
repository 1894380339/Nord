# Generated by Django 4.0.3 on 2022-04-10 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_md_contact_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='md_contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 14, 58, 21, 248639)),
        ),
    ]
