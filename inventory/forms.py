from django import forms
from .models import Material, Product, ProductMaterial
from django.forms import inlineformset_factory

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'price', 'quantity', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'selling_price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ['material', 'quantity']
        widgets = {
            'material': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})
        }

# Create a formset for managing multiple ProductMaterial instances
ProductMaterialFormSet = inlineformset_factory(
    Product,
    ProductMaterial,
    form=ProductMaterialForm,
    extra=1,
    can_delete=True
)
