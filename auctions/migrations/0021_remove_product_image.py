# Generated by Django 4.0.4 on 2022-08-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_comment_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]