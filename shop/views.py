from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from backendApp.models import Product

# Create your views here.


def index(req):
    
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        context = {'name' : req.user.username}
        return render(req, 'index.html',context)
    else:
        return redirect('/shop/login')



def catalog(req):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        products = Product.objects.all()
        context = {'name' : req.user.username,
                    'products' : products
                   }         
        return render(req, 'catalog.html',context)
    else:
        return redirect('/shop/login')
    



def product_detail(req, id):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        product = get_object_or_404(Product, id=id)
        context = {'name' : req.user.username,
                   'product' : product
                   }
        return render(req, 'product_detail.html',context)
    else:
        return redirect('/shop/login')


def orders(req):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        context = {'name' : req.user.username}
        return render(req, 'orders.html',context)
    else:
        return redirect('/shop/login')


def checkout(req):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        context = {'name' : req.user.username}
        return render(req, 'checkout.html',context)
    else:
        return redirect('/shop/login')


def user_register(req):
    if (req.method == 'POST'):
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        try:
            if User.objects.filter(username=username).exists():
                return redirect('/shop/register')
        except Exception as e:
            messages.error(req, "Username is already taken.")
            return redirect('/shop/register')

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        messages.success(req, "Registration successful. You can now log in.")
        return redirect('/shop/login')

    return render(req, 'user_register.html')


def user_login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        # Authenticate the user
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "Login successful.")
            # Redirect to dashboard or wherever you like
            return redirect('/')
        else:
            messages.error(req, "Invalid username or password!")
            return redirect('/shop/login')
    return render(req, 'user_login.html')


def user_logout(req):
    logout(req)
    messages.success(req, "You have been logged out.")
    return redirect('/shop/login')
