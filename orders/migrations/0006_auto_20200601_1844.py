# Generated by Django 3.0.6 on 2020-06-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200601_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incart',
            name='product_id',
            field=models.IntegerField(verbose_name='product_id'),
        ),
    ]
