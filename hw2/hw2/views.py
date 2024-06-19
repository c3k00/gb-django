from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order, OrderItem
from django.http import HttpResponse

def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    return render(request, 'index.html', context)

def clients_list(request):
    """Отображение списка клиентов"""
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

def create_client(request):
    """Создание нового клиента"""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Client.objects.create(name=name, email=email, phone=phone)
        return redirect('clients_list')
    return render(request, 'create_client.html')

def products_list(request):
    """Отображение списка товаров"""
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def create_product(request):
    """Создание нового товара"""
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description', '')
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
        return redirect('products_list')
    return render(request, 'create_product.html')

def orders_list(request):
    """Отображение списка заказов"""
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})

def create_order(request):
    """Создание нового заказа"""
    if request.method == 'POST':
        client_id = request.POST['client']
        product_ids = request.POST.getlist('products')
        client = get_object_or_404(Client, id=client_id)
        order = Order.objects.create(client=client)
        for product_id in product_ids:
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=1)
        order.save()  # Не забудьте сохранить заказ, чтобы обновить общую сумму
        return redirect('orders_list')
    clients = Client.objects.all()
    products = Product.objects.all()
    return render(request, 'create_order.html', {'clients': clients, 'products': products})

def order_detail(request, order_id):
    """Отображение деталей заказа"""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

def product_detail(request, product_id):
    """Отображение деталей товара"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})