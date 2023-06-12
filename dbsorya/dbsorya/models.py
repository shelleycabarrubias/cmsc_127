from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

class Product(models.Model):
    product_code = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_acquired = models.DateField()
    expiration_date = models.DateField()
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    storage_location = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='check_category',
                check=models.Q(category__name='food_item') | models.Q(category__name='non_food_item')
            )
        ]
