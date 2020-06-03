from django.db import IntegrityError
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from orders.models import Product, InCart, Payment, PlacedOrder, OrderDetail
from cart.cart import Cart
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.


def index(request):
    # return HttpResponse("Project 3: TODO")
    # context = {
    #     'orders': Product.objects.all(),
    #     # 'products': Product.objects.filter(category='Dinner Plates').order_by('productName').values_list('productName',
    #     #                                                                                                  flat=True).distinct()
    #
    # }

    context ={
        'dinners': Product.objects.values('id','productName', 'size', 'unitPrice').filter(category='Dinner Plates').order_by('productName', 'unitPrice'),
        'regular_pizza': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Regular Pizza').order_by('productName', 'unitPrice'),
        'sicilian_pizza': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Sicilian Pizza').order_by('productName', 'unitPrice'),
        'subs': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Subs').order_by('productName', 'unitPrice'),
        'salads': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Salads').order_by('productName', 'unitPrice'),
        'pasta': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Pastas').order_by('productName', 'unitPrice'),
        'pizza_toppings': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Pizza Toppings').order_by('productName', 'unitPrice'),
        'subs_toppings': Product.objects.values('id', 'productName', 'size', 'unitPrice').filter(
            category='Subs Toppings').order_by('productName', 'unitPrice'),
        'cart': Cart(request),
        'cart_from_db': InCart.objects.values('product','quantity','cart_id', 'unit_price', 'total', 'product__category',
                                                    'product__size', 'product__productName').filter(user=request.user.id)
    }
    return render(request, 'orders/index.html', context)

def signup(request):
    if request.POST:
        try:
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(email, email, password, first_name=firstName, last_name=lastName)
            return render(request, 'orders/signup.html', {'message': 'Account created with success'})
        except IntegrityError:
            return render(request, 'orders/signup.html', {'message': 'Email already registered'})
    return render(request, 'orders/signup.html')

def signin(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('store'))
        else:
            return render(request, 'orders/signin.html', {'message': "Your username and password didn't match. Please try again"})
    return render(request, 'orders/signin.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('store'))

def add_to_cart(request, product_id, anchor):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unitPrice, 1)
    if request.user.is_authenticated:
        user = request.user.id
        for item in cart:
            to_db = InCart(product_id=product_id, user=user, unit_price=product.unitPrice, quantity=item.quantity, total=item.total_price, cart_id=item.cart_id)
        to_db.save()
    return HttpResponseRedirect(reverse(anchor).replace('%23', '#'))

def remove_from_cart(request, product_id, cart_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    if request.user.is_authenticated:
       InCart.objects.filter(product_id=product_id, cart_id=cart_id).delete()
    return HttpResponseRedirect(reverse('in_cart').replace('%23', '#'))


def proceed_checkout(request):
    context = {

        'cart': Cart(request),
        'cart_from_db': InCart.objects.values('product', 'quantity', 'cart_id', 'unit_price', 'total',
                                              'product__category',
                                              'product__size', 'product__productName').filter(user=request.user.id)
    }

    return render(request, 'orders/checkout.html', context)

def payment(request):
    token = request.POST.get('stripeToken')
    cart = Cart(request)
    cart_from_db = InCart.objects.all().filter(user=request.user.id)
    order = PlacedOrder()
    if request.user.is_authenticated:
        amount = 0
        for data in cart_from_db:
            amount += data.unit_price
    else:
        amount = cart.summary()

    try:
        charge = stripe.Charge.create(
            amount=int(amount)*100,
            currency="usd",
            source=token
        )

        if request.user.is_authenticated:
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user_id = request.user.id
            payment.amount = amount
            payment.save()
            order.user_id = request.user.id
            order.order_total = amount
            order.save()
            for data in cart_from_db:
                items = OrderDetail(items_id=data.product_id, quantity=data.quantity, unit_price=data.unit_price, placed_order_id=order.id)
            items.save()
            InCart.objects.all().delete()
        else:
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user_id = 3
            payment.amount = amount
            payment.save()
            order.user_id = 3
            order.order_total = amount
            order.save()
            for data in cart:
                items = OrderDetail(items_id=data.product, quantity=data.quantity, unit_price=data.unit_price,
                                    placed_order_id=order.id)
            items.save()
            cart.clear()
        return render(request, 'orders/index.html', {'message': "Thank you your online order was placed successfully"})
    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught
        return HttpResponseRedirect(reverse('proceed_checkout', {'message': "Card declined. Please try again"}))
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        pass
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        return HttpResponseRedirect(reverse('proceed_checkout', {'message': "InvalidRequestError"}))
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        return HttpResponseRedirect(reverse('proceed_checkout', {'message': "AuthenticationError"}))
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        return HttpResponseRedirect(reverse('proceed_checkout', {'message': "APIConnectionErro"}))
    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        return HttpResponseRedirect(reverse('proceed_checkout', {'message': "Something went wrong you were not charged. Please try again"}))
    except Exception as e:
        return HttpResponseRedirect(reverse('proceed_checkout', {'message': "Something went wrong with Pizza Mar"}))



















