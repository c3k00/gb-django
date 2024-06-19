"""
URL configuration for hw2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients_list, name='clients_list'),
    path('clients/create/', views.create_client, name='create_client'),
    path('products/', views.products_list, name='products_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]
