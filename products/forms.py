from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title', 'tabindex':'4'}),
            'description': forms.Textarea(attrs={'class': 'form-control w-250', 'placeholder': 'Write the description', 'tabindex':'5'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': '100', 'step': '100', 'placeholder': 'Enter the price', 'tabindex':'6'}),
            'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'tabindex':'7'})
        }