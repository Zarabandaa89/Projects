from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages


def index(request):
    return render(request, 'register.html', {
        # contexto
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, '')
            return redirect('main')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

        return render(request, 'login.html', {

        })

    return render(request, 'login.html', {

    })


def register_view(request):
    return render(request, 'register.html', {

    })


def products_view(request):
    return render(request, 'products.html')


def profile_view(request):
    return render(request, 'profile.html')


def customer_service_view(request):
    return render(request, 'customer_service.html')


def main_view(request):
    return render(request, 'main.html')


def we_view(request):
    return render(request, 'we.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada Gracias por visitarnos')
    return redirect('login')
