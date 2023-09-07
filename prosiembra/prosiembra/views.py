from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages



def index(request):
    return render(request,'users/login.html',{
            #contexto
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
                        messages.success(request, 'Bienvenido {}' .fotmat(user.username))
                        return redirect('products')
                else:
                    messages.error(request, 'Usuario o contraseña incorrectos')
                    
                    return render(request, 'products/products.html',{
                    
            })




def register_view(request):
       if request.method == 'POST':
              username = request.POST.get('name')
              password = request.POST.get('password')
              email = request.POST.get('email')

              print(username)
              print(password)
              print(email)

              user = authenticate(username=username, password=password, email=email)
              if user:
                    register_view(request, user)
                    return redirect('login')
              
       return render(request, 'user/register.html')






def products_view(request):
              
       return render(request, 'products/products.html' )