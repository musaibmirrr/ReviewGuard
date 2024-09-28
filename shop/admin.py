from django.contrib import admin
from .models import Order,Review,Shop_session
# Register your models here.
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Shop_session)