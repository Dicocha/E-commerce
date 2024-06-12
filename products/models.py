from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_image/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the image name based on the product name
        if self.image:
            extension = self.image.name.split('.')[-1]
            new_name = slugify(self.name)  # Using slugify to create a valid filename
            self.image.name = f'{new_name}.{extension}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name