# Generated by Django 2.2 on 2022-03-28 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220327_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='prodct',
            new_name='product',
        ),
    ]