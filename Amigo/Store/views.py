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

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success('User Created SuccessFully')
            print('created')
            return redirect(landing)
        else:
            print('not match')
    return HttpResponse('Not Authorized')