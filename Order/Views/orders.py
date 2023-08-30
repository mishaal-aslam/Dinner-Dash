from django.shortcuts import render, redirect
from django.views import View
from Items.Models.items import Items
from Items.Models.customer import Customer
from Order.Models.order import Order


class Cart(View):
    def get(self, request):
        item_ids = list(request.session.get('cart').keys())
        items = Items.objects.filter(item_id__in=item_ids)
        return render(request, 'order/cart.html', {'items': items})


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        item_ids = list(cart.keys())
        items = Items.objects.filter(item_id__in=item_ids)
        for item in items:
            order = Order(customer=Customer(id=customer), item=item, price=item.price,
                          quantity=cart.get(str(item.item_id)), address=str())
            order = Order(customer=Customer(id=customer), item=item, price=item.price,
                          quantity=cart.get(str(item.item_id)), address=str(address))
            order.save()
        request.session['cart'] = {}
        return redirect('cart')


class Orders(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.objects.filter(customer=customer).order_by('-date')
        return render(request, 'order/orders.html', {'orders': orders})
