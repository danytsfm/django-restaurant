# Generated by Django 3.0.6 on 2020-06-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200601_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incart',
            name='cart_id',
            field=models.IntegerField(verbose_name='cart_id'),
        ),
    ]
