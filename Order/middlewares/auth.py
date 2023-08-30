
from django.shortcuts import render, redirect

from django.urls import reverse


def auth_middleware(get_response):

    def middleware(request):
        return_url = request.get_full_path()
        login_url = reverse('login')
        if not request.session.get('customer'):
            return redirect(f'{login_url}?return_url={return_url}')
        response = get_response(request)

        return response

    return middleware
