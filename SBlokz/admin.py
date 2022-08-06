from django.contrib import admin
from django.contrib.auth.models import User
from .models import Order, Product, Friend

admin.site.site_header = 'Admin Dashboard'

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Friend)