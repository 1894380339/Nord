# Generated by Django 2.2 on 2022-03-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_img_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_product',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
