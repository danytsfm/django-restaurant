# Generated by Django 3.0.6 on 2020-06-01 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200601_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Product', verbose_name='product_id'),
        ),
        migrations.AlterField(
            model_name='incart',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=0, verbose_name='total'),
        ),
    ]