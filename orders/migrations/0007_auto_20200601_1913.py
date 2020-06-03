# Generated by Django 3.0.6 on 2020-06-01 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200601_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incart',
            old_name='product_id',
            new_name='p_id',
        ),
        migrations.AddField(
            model_name='incart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Product', verbose_name='product_desc'),
            preserve_default=False,
        ),
    ]
