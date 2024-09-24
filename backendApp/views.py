from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def admin_check(user):
    return user.is_superuser or user.is_staff

@login_required
@user_passes_test(admin_check)
def index(req):
    return render(req, 'dashboard.html')

@login_required
@user_passes_test(admin_check)
def viewproducts(req):
    products = Product.objects.all()
    return render(req, 'viewproducts.html', {'products': products})

@login_required
@user_passes_test(admin_check)
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

@login_required
@user_passes_test(admin_check)
def allorders(req):
    return render(req, 'allorders.html')

@login_required
@user_passes_test(admin_check)
def users(req):
    return render(req, 'users.html')


def login(req):
    if req.method == 'POST': 
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/reviewGuard')
        else:
            return render(req, 'login.html')

    return render(req, 'login.html')
