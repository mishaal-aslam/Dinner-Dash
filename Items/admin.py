from django.contrib import admin
from .models import Category , Items, Customer
from Order.models import Order

class AdminItems(admin.ModelAdmin):
    list_display=['title', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']


# Register your models here.
admin.site.register(Category , AdminCategory)
admin.site.register(Items, AdminItems)
admin.site.register(Customer)
admin.site.register(Order)