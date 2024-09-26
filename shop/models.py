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

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    body = models.TextField()
    ipAddress = models.GenericIPAddressField(default='127.0.0.1')
    ipCount = models.IntegerField(default=1)
    isVerified = models.BooleanField(default=False)
    subjectivity = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    polarity = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    isFake = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username