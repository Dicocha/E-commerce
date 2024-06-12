from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
 
    def subtotal(self):
        return self.product.price * self.quantity

    def order_number(self):
        return f"Order #{self.id} - {self.user.username}"