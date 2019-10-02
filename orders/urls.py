from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name='register'),
    path("enter", views.enter, name='enter'),
    path("exit", views.exit, name='exit'),
    path("pizza/<id>/<item>", views.process_order, name='process_order'),
    path("cart/<order_id>", views.process_cart, name='process_cart'),
    path("display_orders", views.display_orders, name='display_orders'),
    path("clear_cart", views.clear_cart, name='clear_cart')


]