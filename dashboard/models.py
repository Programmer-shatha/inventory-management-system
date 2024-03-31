from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Computer and laptop', 'Computer and laptop'),
    ('smart phone', 'smart phone'),
    ('devices supplies', 'devices supplies'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'
    

class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.username}-{self.name}'
