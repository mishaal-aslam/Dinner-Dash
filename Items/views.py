from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from .models import Items, Category, Customer
from Order.models import Order
from .utils import validate_password, emailexists


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


class Signup(View):
    def get(self, request):
        return render(request, 'items/signup.html')

    def post(self, request):
        name = request.POST.get('name')
        display_name = request.POST.get('displayname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        value = {'name': name,
                 'display_name': display_name,
                 'email': email}
        customer = Customer(name=name,
                            display_name=display_name,
                            email=email,
                            password=password)
        error_message = None
        errormessage = validate_password(
            password, confirm_password)
        if (not name):
            error_message = 'Name Required'
        elif (len(name) < 7):
            error_message = 'Name must be 7 characters long'
        elif errormessage:
            error_message = errormessage
        elif emailexists(email):
            error_message = 'This email already exists'

        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('home')
        else:
            context = {'error': error_message, 'values': value}
            return render(request, 'items/signup.html', context)


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'items/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email)
        except:
            customer = None
        error_message = None
        if customer:
            if check_password(password, customer.password):
                request.session['customer'] = customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = 'Invalid Email or Password'
        else:
            error_message = 'Invalid Email or Password'
        return render(request, 'items/login.html', {'error': error_message})


class Cart(View):
    def get(self, request):
        item_ids = list(request.session.get('cart').keys())
        items = Items.objects.filter(item_id__in=item_ids)
        return render(request, 'items/cart.html', {'items': items})


def logout(request):
    request.session.clear()
    return redirect('login')


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        item_ids = list(cart.keys())
        items = Items.objects.filter(item_id__in=item_ids)
        print(items)
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
        return render(request, 'items/orders.html', {'orders': orders})
