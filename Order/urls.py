from django.urls import path
from .Views import orders
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('cart/', orders.Cart.as_view(), name="cart"),
    path('checkout/', auth_middleware(orders.Checkout.as_view()), name="checkout"),
    path('orders/', auth_middleware(orders.Orders.as_view()), name="orders")
]
