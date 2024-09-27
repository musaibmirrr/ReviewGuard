from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from shop.models import Order,Review

# Create your views here.

def index(req):
    if req.user.is_authenticated and req.user.is_superuser:
        reviews = Review.objects.all()
        context = {
            'reviews' : reviews
        }
        return render(req, 'dashboard.html',context)
    else:
        return redirect('/reviewGuard/login')


def viewproducts(req):
    if req.user.is_authenticated and req.user.is_superuser:
        products = Product.objects.all()
        return render(req, 'viewproducts.html', {'products': products})
    else:
        return redirect('/reviewGuard/login')


def addproducts(req):
    if req.user.is_authenticated  and req.user.is_superuser:
        if (req.method == 'POST'):
            name = req.POST.get('productname')
            description = req.POST.get('description')
            price = req.POST.get('price')
            mrp = req.POST.get('mrp')
            image = req.FILES.get('image')
            product = Product(name=name, description=description,
                          price=price, mrp=mrp, image=image)
            product.save()
            messages.success(req, 'Product added successfully!')
            return redirect('/reviewGuard/viewproducts')
        return render(req, 'addproducts.html')
    else:
        return redirect('/reviewGuard/login')




def allorders(req):
    if req.user.is_authenticated  and req.user.is_superuser:
        orders = Order.objects.all() 
        context = {'orders' : orders}
        return render(req, 'allorders.html',context)
    else:
        return redirect('/reviewGuard/login')

def view_users(req):
    if req.user.is_authenticated  and req.user.is_superuser:
        users = User.objects.all()   
        return render(req, 'view_users.html',{'users' : users})
    else:
        return redirect('/reviewGuard/login')


def admin_login(req):
    if (req.method == 'POST'):
        username = req.POST.get('username')
        password = req.POST.get('password')
        # authentication
        user = authenticate(req, username=username, password=password)


        if user is not None:
          if(user.is_superuser):
            # Log the user in and redirect to a protected page (like admin dashboard)
            login(req, user)
            messages.success(req, f'Welcome back, {req.user.username}')
            # Replace with your desired redirect URL
            return redirect('/reviewGuard')
          else:
            messages.error(req, 'A user cannot access admin page!')
            return redirect('/reviewGuard/login')
        else:
            # Invalid login credentials
            messages.error(req, 'Invalid username or password')
            return redirect('/reviewGuard/login')

    return render(req, 'admin_login.html')



def admin_logout(req):
    if req.user.is_authenticated and req.user.is_superuser:
        if (req.method == 'POST'):
            logout(req)
            messages.success(req, 'You have signed out!')
            return redirect('/reviewGuard/login')
        else:
            messages.error(req, 'Cannot proceed that request!')
            return redirect('/reviewGuard')
    messages.error(req, 'You dont have permission to do that!')    
    return redirect('/reviewGuard/login')
    # Redirect to login after logging out
