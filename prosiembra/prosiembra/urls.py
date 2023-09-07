from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/register', views.register_view, name='register'),
    path('productos/', views.products_view, name='products'),

    path('admin/', admin.site.urls),
  
]
