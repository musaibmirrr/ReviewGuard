from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required
def index(req):
    return render(req, 'dashboard.html')

# @login_required
def viewproducts(req):
    products = Product.objects.all()
    return render(req, 'viewproducts.html', {'products': products})

# @login_required
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
        return redirect('/reviewGuard/viewproducts')
    return render(req, 'addproducts.html')

# @login_required
def allorders(req):
    return render(req, 'allorders.html')

# @login_required
def users(req):
    return render(req, 'users.html')


def login(req):
    if (req.method == 'POST'):
        username = req.POST.get('username')
        password = req.POST.get('password')
        # authentication
        user = authenticate(req, username=username, password=password)

        if user is not None:
            # Log the user in and redirect to a protected page (like admin dashboard)
            login(req, user)
            # Replace with your desired redirect URL
            return redirect('/reviewGuard')
        else:
            # Invalid login credentials
            return redirect('/reviewGuard/login')

    return render(req, 'login.html')
