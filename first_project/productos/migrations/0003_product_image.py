# Generated by Django 4.2.3 on 2023-07-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='productos/'),
            preserve_default=False,
        ),
    ]