from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from backendApp.models import Product
from shop.models import Order,Review
from textblob import TextBlob


#utility function to get ip of client
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def index(req):
    if (req.user.is_authenticated) and (not req.user.is_superuser):
            context = {'name': req.user.username}
            return render(req, 'index.html',context)
    else:
        return redirect('/shop/login')


def catalog(req):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        products = Product.objects.all()
        context = {'name': req.user.username,
                   'products': products
                   }
        return render(req, 'catalog.html', context)
    else:
        return redirect('/shop/login')


def product_detail(req, id):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        product = get_object_or_404(Product, id=id)
        isVerified = False       
        
        if(req.method == 'POST'):
            rating = req.POST.get('rating')
            body = req.POST.get('body')

            #ip code
            ipAddress = get_client_ip(req)
            review_count = Review.objects.filter(ipAddress=ipAddress, product=product).count()
            ipCount = review_count + 1

            #text blob code
            blob = TextBlob(body)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

             #isVerified check
            orders = Order.objects.filter(user=req.user)
            for order in orders:
                if order.product.id == id:
                    isVerified = True 
            
            
            if polarity > 0.9:
                if subjectivity <= 0.5:
                    isFake = False    
                else:
                    if (isVerified):
                        isFake = False
                    else:    
                        isFake = True
                        messages.error(req, "Your review seems suspicious.")
            elif polarity < -0.5:
                 if subjectivity <= 0.5:
                    isFake = False
                 else:
                    if(isVerified):
                       isFake = False
                    else:
                        isFake = True
                        messages.error(req, "Your review seems suspicious.")
            else:
                isFake = False


            if review_count > 2:
                messages.error(req, "You have already submitted 3 reviews for this product. Thank you.")
                review = Review(user=req.user,product=product,rating=rating,body=body,ipAddress=ipAddress,ipCount=ipCount,subjectivity=subjectivity,polarity=polarity,isFake=isFake,isVerified=isVerified)
                review.save()
                return redirect(f'/shop/product/{id}')

            
            review = Review(user=req.user,product=product,rating=rating,body=body,ipAddress=ipAddress,ipCount=ipCount,subjectivity=subjectivity,polarity=polarity,isFake=isFake,isVerified=isVerified)
            review.save()
            messages.success(req,"You successfully made a review!")
            return redirect(f'/shop/product/{id}')
        
        
        all_reviews = Review.objects.filter(product=product)
        reviews = []
        for review in all_reviews:
            if review.isFake is False and review.ipCount <= 3:
                reviews.append(review)   
        
        context = {'name': req.user.username,
                   'product': product,
                   'reviews' : reviews
                   }
        return render(req, 'product_detail.html', context)
    else:
        return redirect('/shop/login')


def orders(req):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        user_orders = Order.objects.filter(user=req.user)
        context = {'name': req.user.username,
                   'orders' : user_orders}
        return render(req, 'orders.html', context)
    else:
        return redirect('/shop/login')


def checkout(req,id):
    if ((req.user.is_authenticated) and (not req.user.is_superuser)):
        product = get_object_or_404(Product, id=id)

        if req.method == 'POST':
            address = req.POST.get('address')
            city = req.POST.get('city')
            state = req.POST.get('state')
            landmark = req.POST.get('landmark')
            payment = req.POST.get('payment')

            order = Order(user=req.user, product=product, address=address,city=city, state=state, landmark=landmark,payment=payment)
            order.save()
            messages.success(req,"Your order has been placed successfully!")
            return redirect('/shop/orders')
        
        context = {'name': req.user.username,
                   'product' : product}
        return render(req, 'checkout.html', context)
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
           if(not user.is_superuser): 
            login(req, user)
            messages.success(req, "Login successful.")
            # Redirect to dashboard or wherever you like
            return redirect('/')
           else:
            messages.error(req,"You are not a user!")
            return redirect('/shop/login')

        else:
            messages.error(req, "Invalid username or password!")
            return redirect('/shop/login')
    return render(req, 'user_login.html')


def user_logout(req):
    logout(req)
    messages.success(req, "You have been logged out.")
    return redirect('/shop/login')

def aboutus(req):
   context={
      'name': req.user.username,
   }
   return render(req,'aboutus.html',context)
