# Generated by Django 4.0.4 on 2022-08-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_product_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.TextField(blank=True, max_length=4294967295, null=True),
        ),
    ]
