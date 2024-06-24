from django import forms
from .models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
        
class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple  # или другой виджет по вашему выбору
    )

    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount']