from django.contrib import admin
from .models import Inventory,Product,Rendezvous,Sale,Customer_Service

admin.site.register(Inventory)

admin.site.register(Product)

admin.site.register(Rendezvous)

admin.site.register(Sale)

admin.site.register(Customer_Service)
