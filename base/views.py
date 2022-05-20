from django.http import JsonResponse
from django.shortcuts import render
import os 
import math

from base.models import Product

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def shop(request):
    return render(request, 'base/shop.html')

# Utils

def number_pages():
    try:
        products = list(Product.objects.all().values())
        length = len(products)
        return math.ceil(length/12)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    
# API

def get_products(request):
    try:
        products = list(Product.objects.all().values())
        return JsonResponse({'products':products})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def get_products_by_page(request,page):
    try:
        products = list(Product.objects.all().values()[(page-1)*12:page*12])
        return JsonResponse({'products':products})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def get_number_pages(request):
    try:
        nbPage = number_pages()
        return JsonResponse({'nbPage':nbPage})
    except Exception as e:
        return JsonResponse({'error':str(e)})