from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name
        }

class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    quantity    = models.IntegerField(default=1)
    price       = models.FloatField()
    description = models.TextField()

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    def to_json(self):
        return {
            'id':self.id,
            'category':self.category.to_json(),
            'quantity':self.quantity,
            'price':self.price,
            'description':self.description
        }