from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = names
            user.last_name = username
            user.save()
            
            login(request, user)
            
            messages.success(request, '')
            
            return redirect('main')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


def register_login(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = names
            user.last_name = username
            user.save()
            
            login(request, user)
            
            messages.success(request, '')
            
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'login.html', {
        'form': form
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


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = names
            user.last_name = username
            user.save()
            
            login(request, user)
            
            messages.success(request, '')
            
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
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

