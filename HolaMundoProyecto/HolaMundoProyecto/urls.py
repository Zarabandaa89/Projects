from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_mundo, name='inicio'),
    path('hola/', views.hola_mundo, name='hola_mundo'),
]
