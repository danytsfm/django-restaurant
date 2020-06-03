from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("store", views.index, name="store"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add_to_cart/<int:product_id>/<str:anchor>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/<int:cart_id>', views.remove_from_cart, name='remove_from_cart'),
    path('store#in_cart', views.index, name='in_cart'),
    path('#sic_pizzas', views.index, name='sic_pizzas'),
    path('#salads', views.index, name='salads'),
    path('#subs', views.index, name='subs'),
    path('#reg_pizzas', views.index, name='reg_pizzas'),
    path('#dinners', views.index, name='dinners'),
    path('#pastas', views.index, name='pastas'),
    path("checkout", views.proceed_checkout, name='proceed_checkout'),
    path('payment', views.payment, name='payment')
]
