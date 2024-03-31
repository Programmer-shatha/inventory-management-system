from django import forms
from .models import Product ,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'category':forms.Select(attrs={'class':'form-select'}),
        'quantity':forms.TextInput(attrs={'class':'form-control'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'order_quantity']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'order_quantity':forms.TextInput(attrs={'class':'form-control'})
        }