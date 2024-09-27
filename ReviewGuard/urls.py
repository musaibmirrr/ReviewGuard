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
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def csrf_failure(request, reason=""):
    return HttpResponse(f'CSRF Failure: {reason}', status=403)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('csrf-debug/', csrf_exempt(csrf_failure)),
    #frontend routes
    path('',shopview.index),
    path('shop/',shopview.catalog),
    path('shop/product/<int:id>/',shopview.product_detail),
    path('shop/orders/',shopview.orders),
    path('shop/product/<int:id>/checkout/',shopview.checkout),
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