from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order, OrderItem
from .forms import ClientForm, ProductForm
def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    return render(request, 'index.html', context)

# Клиенты
def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

def client_detail(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'client_detail.html', {'client': client})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('clients_list')
    return render(request, 'delete_client.html', {'client': client})

# Продукты
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    return render(request, 'delete_product.html', {'product': product})

# Заказы
def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})

def create_order(request):
    clients = Client.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        client_id = request.POST['client']
        product_ids = request.POST.getlist('products')
        client = get_object_or_404(Client, id=client_id)
        order = Order.objects.create(client=client)
        for product_id in product_ids:
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(order=order, product=product)
        return redirect('orders_list')
    return render(request, 'create_order.html', {'clients': clients, 'products': products})

def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    clients = Client.objects.all()
    products = Product.objects.all()
    order_products = [item.product.id for item in order.items.all()]
    if request.method == 'POST':
        order.client = get_object_or_404(Client, id=request.POST['client'])
        order.items.all().delete()
        for product_id in request.POST.getlist('products'):
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(order=order, product=product)
        order.save()
        return redirect('orders_list')
    return render(request, 'edit_order.html', {
        'order': order,
        'clients': clients,
        'products': products,
        'order_products': order_products,
    })

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('orders_list')
    return render(request, 'delete_order.html', {'order': order})