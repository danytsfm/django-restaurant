from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=50)
    productName = models.CharField(max_length=50)
    size = models.CharField(max_length=8, null='small')
    unitPrice = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return f'{self.id} - {self.category} {self.productName} {self.size} ${self.unitPrice}'

class InCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product_id')
    user = models.IntegerField()
    unit_price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='unit_price')
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=19, decimal_places=2, null=0, verbose_name='total')
    cart_id = models.IntegerField(verbose_name='cart_id')

    def __str__(self):
        return f'{self.product_id}{self.product} {self.unit_price} {self.cart_id} {self.quantity} {self.total}{self.user}'

class PlacedOrder(models.Model):
    user_id = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=19, decimal_places=2)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f'{self.user_id} {self.order_date} {self.order_total}'

class OrderDetail(models.Model):
    items_id = models.IntegerField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='unit_price')
    placed_order_id = models.IntegerField( blank=True, null=True, verbose_name='placed_order_id')
    def __str__(self):
        return f'{self.placed_order_id} {self.items_id} {self.quantity} {self.unit_price}'

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user_id = models.IntegerField()
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} - {self.amount} - {self.timestamp}'


