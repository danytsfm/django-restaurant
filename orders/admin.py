from django.contrib import admin
from .models import Product, InCart, PlacedOrder, OrderDetail, Payment
# Register your models here.
admin.site.register(Product)
admin.site.register(InCart)
admin.site.register(PlacedOrder)
admin.site.register(OrderDetail)
admin.site.register(Payment)
