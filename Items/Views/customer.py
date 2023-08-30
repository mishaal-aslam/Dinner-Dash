
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from Items.Models.customer import Customer
from Items.utils import validate_password, emailexists


class Signup(View):
    # return_url = None
    def get(self, request):
        # Signup.return_url = request.GET.get('return_url')
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
            error_message = "Your 'Full' Name must be 7 characters long"
        elif errormessage:
            error_message = errormessage
        elif emailexists(email):
            error_message = 'This email already exists'

        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            # if Signup.return_url:
            #         return HttpResponseRedirect(Signup.return_url)
            # else:
            #         Signup.return_url = None
            #         return redirect('home')
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
        email_value = {'email': email}
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
        context = {'error': error_message, 'email_value': email_value}
        return render(request, 'items/login.html', context)


def logout(request):
    customer_id = request.session.get('customer')
    request.session.clear()
    return redirect('login')
