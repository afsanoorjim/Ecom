from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def landing(request):
    products = Product.objects.all()
    context = {
        'products': products, 
    }
    return render(request, 'index.html', context)