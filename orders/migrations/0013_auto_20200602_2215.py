# Generated by Django 3.0.6 on 2020-06-03 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200602_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placedorder',
            name='order_status',
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='placed_order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.PlacedOrder'),
        ),
    ]
