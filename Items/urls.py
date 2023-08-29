from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.Cart.as_view(), name="cart"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('orders/', views.Orders.as_view(), name="orders")
]
