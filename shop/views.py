from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'index.html')

def catalog(req):
    return render(req, 'catalog.html')

def product(req):
    return render(req, 'product.html')

def orders(req):
    return render(req, 'orders.html')

def checkout(req):
    return render(req, 'checkout.html')

def register(req):
    return render(req, 'register.html')

def user_login(req):
    return render(req, 'user_login.html')