from django.contrib import admin
from .models import *
# Register your models here.


class ProductDisplay(admin.ModelAdmin):
    list_display = ['product_name', 'product_price']


admin.site.register(Product, ProductDisplay)

