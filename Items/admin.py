from django.contrib import admin
from Items.Models.category import Category
from Items.Models.items import Items
from Items.Models.customer import Customer


class AdminItems(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, AdminCategory)
admin.site.register(Items, AdminItems)
admin.site.register(Customer)
