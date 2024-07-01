from time import timezone
from django.db import models
from django.utils import timezone
#import datetime

class Client(models.Model):
    """Модель клиента"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    """Модель заказа"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Считаем общую сумму заказа
        self.total_amount = sum(item.product.price * item.quantity for item in self.orderitem_set.all())
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"

class OrderItem(models.Model):
    """Связующая модель для заказов и товаров"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
