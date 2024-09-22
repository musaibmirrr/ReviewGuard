from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'dashboard.html')

def viewproducts(req):
    return render(req, 'viewproducts.html')

def addproducts(req):
    return render(req, 'addproducts.html')

def allorders(req):
    return render(req, 'allorders.html')

def users(req):
    return render(req, 'users.html')

def login(req):
    return render(req, 'login.html')