from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Material(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    image = models.ImageField(upload_to='materials/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    materials = models.ManyToManyField(
        Material,
        through='ProductMaterial',
        related_name='products'
    )

    def __str__(self):
        return self.name

    def material_cost(self):
        total = Decimal('0.00')
        for pm in self.productmaterial_set.all():
            total += pm.material.price * pm.quantity
        return total

    def profit(self):
        return self.selling_price - self.material_cost()

    class Meta:
        ordering = ['name']

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )

    class Meta:
        unique_together = ['product', 'material']

    def __str__(self):
        return f"{self.product.name} - {self.material.name} ({self.quantity})"
