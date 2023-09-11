from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('products/', views.products_view, name='products'),
    path('profile/', views.profile_view, name='profile'),
    path('customer_service/', views.customer_service_view, name='customer'),
    path('main/', views.main_view, name='main'),
    path('we/', views.we_view, name='we'),
    path('logout/', views.logout_view, name='logout'),

    
]
