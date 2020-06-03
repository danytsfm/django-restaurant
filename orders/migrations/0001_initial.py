# Generated by Django 3.0.6 on 2020-06-01 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('cart_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('productName', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=8, null='small')),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='PlacedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('order_date', models.DateField()),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('order_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placed_order', to='orders.InCart')),
            ],
        ),
        migrations.AddField(
            model_name='incart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='orders.Product'),
        ),
    ]
