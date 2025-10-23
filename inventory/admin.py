from django.contrib import admin
from .models import Material, Product, ProductMaterial

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'selling_price', 'material_cost', 'profit')
    search_fields = ('name',)

@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')
    autocomplete_fields = ('product', 'material')
