from django.urls import path
from . import views
from .middlewares.auth import auth_middleware #,auth_checkout_middleware

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.Cart.as_view(), name="cart"),
    path('checkout/', auth_middleware(views.Checkout.as_view()), name="checkout"),
    path('orders/', auth_middleware(views.Orders.as_view()), name="orders")
]
