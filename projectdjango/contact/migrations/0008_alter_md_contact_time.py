# Generated by Django 4.0.3 on 2022-04-12 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_md_contact_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='md_contact',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 12, 14, 46, 6, 91585)),
        ),
    ]