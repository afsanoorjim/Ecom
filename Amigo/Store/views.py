from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User


def landing(request):
    products = Product.objects.all()
    context = {
        'products': products, 
    }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            User.objects.create_user(username=username, email=email, password=password1)
            messages.success('User Created SuccessFully')
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)