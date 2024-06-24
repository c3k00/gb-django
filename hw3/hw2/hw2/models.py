from django.db import models

class Client(models.Model):
    """Модель клиента"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)  # Убираем editable=False
    products = models.ManyToManyField('Product')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"
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
    
