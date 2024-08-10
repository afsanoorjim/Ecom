from django.shortcuts import render
from .models import *
from .form import RegisterUser
from django.contrib import messages



def landing(request):
    products = Product.objects.all()
    if request.POST == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid:
            form.save()
            messages.success('User Created')
            return render(request, 'index.html', context)
    else:
        form = RegisterUser()


    context = {
        'products': products, 
        'form':form,
    }
    return render(request, 'index.html', context)
