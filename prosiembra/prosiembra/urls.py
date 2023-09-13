from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('login/', views.login_view, name='login'),
    path('login/register.html', views.register, name= 'login a registro'),
    path('login/login', views.login_view),
    path('', views.register, name='register'),
    path('login/register.htmls', views.register),
    #path('/login.html', views.login_view),
    path('products/', views.products_view, name='products'),
    path('profile/', views.profile_view, name='profile'),
    path('customer_service/', views.customer_service_view, name='customer'),
    path('main/', views.main_view, name='main'),
    path('we/', views.we_view, name='we'),
    path('logout/', views.logout_view, name='logout'),

    
]
