from django.db import models

class Inventory(models.Model):
    purchase_order = models.FloatField(verbose_name= 'Orden de compra')
    quantity_products = models.FloatField(verbose_name= 'Cantidad productos')
    existing_products = models.FloatField(verbose_name= 'Productos existentes')
    batches_products = models.FloatField(verbose_name= 'Numero lotes de productos')
    expiration_date = models.DateField(verbose_name= 'Fecha vencimiento')

    def __str__(self):
        return self.purchase_order
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'Inventario'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    expiration_date = models.DateField(verbose_name='Fecha vencimiento')
    serial_number = models.FloatField(verbose_name='Número de serie')
    weight = models.FloatField(verbose_name='Gramaje') 
    price = models.FloatField(verbose_name='Precio')
    quantity = models.FloatField(verbose_name='Cantidad')
    type_presentation = models.CharField(max_length=80, verbose_name='Tipo de presentación', default='default_value')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']


class Rendezvous(models.Model):
    date_time = models.DateTimeField(verbose_name= 'Cita')
    quote_value = models.FloatField(verbose_name= 'Valor cita')
    virtual_onsite = models.CharField(max_length=100, verbose_name= 'Virtual o presencial')
    appointment_status = models.CharField(max_length=100, verbose_name= 'Estado de cita')
    location = models.CharField(max_length=100, verbose_name= 'Ubicacion')
    appointment_type = models.CharField( max_length=100, verbose_name= 'Tipo de cita')
    def __str__(self):
        return self.date_time
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        db_table = 'Cita'
        ordering = ['id']



class Sale(models.Model):
    date_sale = models.DateField(verbose_name= 'Fecha de venta')
    payment_method = models.CharField(max_length=100, verbose_name= 'Metodo de pago')
    coupons_available = models.FloatField(verbose_name= 'Cupones disponibles')
    receipt_number = models.FloatField(verbose_name= 'Numero de recibo')
    unit_value = models.FloatField(verbose_name= 'Valor unitario')
    total_value = models.FloatField(verbose_name= 'Valor total')
    quantity = models.FloatField(verbose_name= 'Cantidad')
    order_number = models.FloatField(verbose_name= 'Numero de orden')
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
        ordering = ['id']



class Customer_Service(models.Model):
    application_date_pqrs = models.DateField(verbose_name= 'Fecha solicitud PQRS')
    response_dates = models.CharField(max_length=100, verbose_name= 'Metodo de respuesta PQRS')
    type_pqrs = models.CharField(max_length=100, verbose_name= 'Tipo PQRS')
    state = models.CharField(max_length=100, verbose_name= 'estado PQRS')
    priority = models.CharField(max_length=100, verbose_name= 'Prioridad')
    
    
    def __str__(self):
        return self.application_date_pqrs
    
    class Meta:
        verbose_name = 'Atencion cliente'
        verbose_name_plural = 'Atencion Clientes'
        db_table = 'Atencion cliente'
        ordering = ['id']