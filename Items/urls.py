from django.urls import path
from .Views import index, customer

urlpatterns = [
    path('', index.Index.as_view(), name='home'),
    path('signup/', customer.Signup.as_view(), name='signup'),
    path('login/', customer.Login.as_view(), name='login'),
    path('logout/', customer.logout, name='logout'),
]
