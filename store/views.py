from django.shortcuts import render
from .models import Product, Category

def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})


