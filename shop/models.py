from django.db import models
from django.contrib.auth.models import User
from backendApp.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    payment = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
