
from django.shortcuts import render, redirect

def auth_middleware(get_response):

    def middleware(request):

        print(request.session.get('customer'))
        return_url=request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?return_url={return_url}')
        response = get_response(request)

     
        return response

    return middleware
