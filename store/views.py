from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib.auth import logout

# Create your views here.
def store(request):
    product_all = Product.objects.all()
    data = {
        "product_all": product_all
    }
    return render(request, 'store/store.html', data)


def categories(request):
    all_categories = Category.objects.all()
    data = {
        "all_categories": all_categories
    }
    return data


def login_view(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')


def logout(request):
    pass