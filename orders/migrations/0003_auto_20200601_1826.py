# Generated by Django 3.0.6 on 2020-06-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200601_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incart',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='unit_price'),
        ),
    ]
