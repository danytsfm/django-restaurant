# Online pizza restaurant

Harvard CS50 program - Web Programming with Python and JavaScript

## Prerequites: 
- Django 3.0+
- Django-cart
- Stripe
- If you are using django 2.0+ you need to add on_delete=models.CASCADE to all foreign
keys, and cart.py change line 2 to from .import models.

Pizza Mar, you can place your online orders and pay with credit card. This application uses Django's built-in users authentication system. You can navigate through the menu
and add to your cart any item, as you can remove them. The app uses the Django-cart app you can 
place orders as anonymous user, or create an account. The payment process is made by Stripe API. 


