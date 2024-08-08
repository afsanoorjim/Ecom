from django.shortcuts import render
from .models import *

def landing(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)
