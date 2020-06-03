# Generated by Django 3.0.6 on 2020-06-02 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_incart_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='placedorder',
            old_name='customer_id',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='placedorder',
            name='order_details_id',
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='unit_price')),
                ('placed_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placed_order', to='orders.PlacedOrder')),
            ],
        ),
        migrations.AddField(
            model_name='placedorder',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Payment'),
        ),
    ]
