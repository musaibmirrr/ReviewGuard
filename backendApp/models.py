from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    mrp = models.IntegerField()
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name
    
