from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum
from decimal import Decimal
from .models import Material, Product, ProductMaterial
from .forms import MaterialForm, ProductForm, ProductMaterialFormSet

def dashboard(request):
    context = {
        'total_materials': Material.objects.count(),
        'total_products': Product.objects.count(),
        'total_sales': Product.objects.aggregate(Sum('selling_price'))['selling_price__sum'] or Decimal('0.00'),
        'total_profit': sum(product.profit() for product in Product.objects.all()),
        'recent_materials': Material.objects.all()[:5],
        'recent_products': Product.objects.all()[:5],
    }
    return render(request, 'inventory/dashboard.html', context)

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'inventory/material_list.html', {'materials': materials})

def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material created successfully.')
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'inventory/material_form.html', {'form': form, 'title': 'Add Material'})

def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material updated successfully.')
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'inventory/material_form.html', {'form': form, 'title': 'Edit Material'})

def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        messages.success(request, 'Material deleted successfully.')
        return redirect('material_list')
    return render(request, 'inventory/confirm_delete.html', {'object': material})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('product_materials', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form, 'title': 'Add Product'})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form, 'title': 'Edit Product'})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_list')
    return render(request, 'inventory/confirm_delete.html', {'object': product})

def product_materials(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        formset = ProductMaterialFormSet(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Product materials updated successfully.')
            return redirect('product_list')
    else:
        formset = ProductMaterialFormSet(instance=product)
    return render(request, 'inventory/assign_materials.html', {
        'product': product,
        'formset': formset
    })
