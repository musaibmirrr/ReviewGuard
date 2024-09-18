from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'index.html')

def catalog(req):
    return render(req, 'catalog.html')

def product(req):
    return render(req, 'product.html')