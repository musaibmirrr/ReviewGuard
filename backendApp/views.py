from django.shortcuts import render, redirect
from .models import Product

# Create your views here.


def index(req):
    return render(req, 'dashboard.html')


def viewproducts(req):
    return render(req, 'viewproducts.html')


def addproducts(req):
    if (req.method == 'POST'):
        name = req.POST.get('productname')
        description = req.POST.get('description')
        price = req.POST.get('price')
        mrp = req.POST.get('mrp')
        image = req.POST.get('image')
        product = Product(name=name, description=description,
                          price=price, mrp=mrp, image=image)
        product.save()
    return render(req, 'addproducts.html')


def allorders(req):
    return render(req, 'allorders.html')


def users(req):
    return render(req, 'users.html')


def login(req):
    return render(req, 'login.html')
