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


urlpatterns = [

    path('admin/', admin.site.urls),
    #frontend routes
    path('',shopview.index),
    path('shop/',shopview.catalog),
    path('shop/product',shopview.product),
    path('orders/',shopview.orders),
    path('checkout/',shopview.checkout),
    path('register/',shopview.register),
    path('login/',shopview.login),


    #backend routes
     path('dash/',backendview.index),
]
