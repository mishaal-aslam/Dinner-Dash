
from django.shortcuts import render, redirect
from django.views import View
from Items.Models.items import Items
from Items.Models.category import Category


class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categories = Category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
            items = Items.objects.filter(category=category_id)
        else:
            items = Items.objects.all()
        context = {
            'items': items,
            'categories': categories,
        }
        return render(request, 'items/index.html', context)

    def post(self, request):
        item_id = request.POST.get('item')
        decrease_quantity = request.POST.get('decrease_quantity')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(item_id)
            if quantity:
                if decrease_quantity:
                    if quantity <= 1:
                        cart.pop(item_id)
                    else:
                        cart[item_id] = quantity - 1
                else:
                    cart[item_id] = quantity + 1

            else:
                cart[item_id] = 1

        else:
            cart = {}
            cart[item_id] = 1
        request.session['cart'] = cart
        print("cart=", request.session['cart'])
        return redirect('home')
