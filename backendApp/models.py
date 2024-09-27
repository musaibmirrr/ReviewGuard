from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,default="nike shirt")
    description = models.CharField(max_length=100,default="No description available")
    price = models.DecimalField(max_digits=10,decimal_places=2,default=1000)
    mrp = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name
    
