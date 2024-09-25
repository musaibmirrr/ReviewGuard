"""
URL configuration for ReviewGuard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views as shopview
from backendApp import views as backendview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    #frontend routes
    path('',shopview.index),
    path('shop/',shopview.catalog),
    path('shop/product',shopview.product),
    path('orders/',shopview.orders),
    path('checkout/',shopview.checkout),
    path('shop/register/',shopview.user_register),
    path('shop/login/',shopview.user_login),
    path('shop/logout/',shopview.user_logout),


    #backend routes
     path('reviewGuard/',backendview.index),
     path('reviewGuard/viewproducts',backendview.viewproducts),

     path('reviewGuard/addproducts',backendview.addproducts),
     
     path('reviewGuard/orders',backendview.allorders),
     path('reviewGuard/view_users',backendview.view_users),
     path('reviewGuard/login',backendview.admin_login),
     path('reviewGuard/signout',backendview.admin_logout)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)