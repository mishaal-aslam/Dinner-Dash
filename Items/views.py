from django.shortcuts import render, redirect
from .models import Items, Category, Customer
import re


def get_all_items_by_category_id(categoryId):
    if categoryId:
        return Items.objects.filter(category=categoryId)
    else:
        return Items.objects.all()


def index(request):
    # Items = None
    categories = Category.objects.all()
    categoryId = request.GET.get('category')
    if categoryId:
        items = get_all_items_by_category_id(categoryId)
    else:
        items = Items.objects.all()
    context = {}
    context['items'] = items
    context['categories'] = categories
    return render(request, 'items/index.html', context)


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


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
    if (password != confirm_password):
        return 'Password and Confirm Password must be same'


def validate_email(email):
    if not email:
        return 'Email is a required field'
    elif not is_valid_email(email):
        return 'Invalid email address'


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        display_name = request.POST.get('displayname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        value = {'name': name,
                 'display_name': display_name,
                 'email': email}
        error_message = None
        # Fields validation before creating customers

        error_message = validate_password(password, confirm_password)

        if emailexists(email):
            error_message = 'This email already exists'

        error_message = validate_email(email)


        if (not name):
            error_message = 'Name Required'
        elif (len(name) < 7):
            error_message = 'Name must be 7 characters long'

        
        if not error_message:
            customer = Customer(name=name,
                                display_name=display_name,
                                email=email,
                                password=password)
            customer.save()
            return redirect('home')
        else:
            context={'error':error_message, 'values': value}
            return render(request, 'items/signup.html', context)

    return render(request, 'items/signup.html')
