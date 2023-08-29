from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from .models import Items, Category, Customer
import re


class Index(View):
    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
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
                    if quantity<=1:
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


def emailexists(email):
    return Customer.objects.filter(email=email).exists()


def validate_password(password, confirm_password):
    if (not password):
        return 'Please enter password'
    elif len(password) < 8:
        return 'Password must be atleast 8 characters long'
    elif not any(char.isdigit() for char in password):
        return 'Password must contain at least 1 digit'
    elif not any(char.isalpha() for char in password):
        return 'Password must contain at least 1 letter'
    elif (password != confirm_password):
        return 'Password and Confirm Password must be same'
    else:
        return False


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
    def get(self, request):
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
                # request.session['email'] = customer.email
                return redirect('home')
            else:
                error_message = 'Invalid Email or Password'
        else:
            error_message = 'Invalid Email or Password'
        return render(request, 'items/login.html', {'error': error_message})


class Cart(View):
    def get(self, request):
        item_ids=list(request.session.get('cart').keys())
        items = Items.objects.filter(item_id__in=item_ids)
        print(items)
        return render(request, 'items/cart.html', {'items': items})


def logout(request):
    request.session.clear()
    return redirect('login')