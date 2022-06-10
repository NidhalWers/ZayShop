from django.http import JsonResponse
from django.shortcuts import render
import os 
import math

from base.models import Product,Footwear,Apparel

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def shop(request):
    return render(request, 'base/shop.html')

def product(request,id): 
    try:  
        product = Footwear.objects.get(id=id)
        typ = 'footwear'
    except:
        product = Apparel.objects.get(id=id)
        typ = 'apparel'
    return render(request, 'base/product.html', {'product':product,'typ':typ})

def cart(request):
    return render(request, 'base/cart.html')


# Utils

def number_pages():
    try:
        products = list(Product.objects.all().values())
        length = len(products)
        return math.ceil(length/12)
    except Exception as e:
        return e
    
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
        for i in range(len(products)-1):
            if len(products[i]['productDisplayName']) > 30:
                products[i]['productDisplayName'] = products[i]['productDisplayName'][:20] + '...'
        return JsonResponse({'products':products,'error':0})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def get_number_pages(request):
    try:
        nbPage = number_pages()
        listPage=[]
        for i in range(nbPage):
            listPage.append(i)
        return JsonResponse({'nbPage':listPage,'maxPage':nbPage})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def get_product(request,id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse({'product':product})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def add_to_cart(request,id,size,quantity):
    try:
        if 'cart' not in request.session:
            request.session['cart'] = []

        cart = request.session['cart']

        isIn = False

        for article in cart:
            if (article['id'] == id) & (article['size'] == size):
                article['quantity'] += quantity
                request.session['cart'] = cart
                isIn = True
        
        if not isIn:
            product = Product.objects.get(id=id)
            cart.append({'id':id,'quantity':quantity,'name':product.productDisplayName,'price':product.price,'link':product.link,'baseColour':product.baseColour,'size':size})
            request.session['cart'] = cart

        return JsonResponse({'error':0})
    except Exception as e:
        print(e)
        return JsonResponse({'error':e})

def get_cart(request):
    try:
        cart = request.session['cart']
        return JsonResponse({'cart':cart})
    except Exception as e:
        return JsonResponse({'error':str(e)})


def get_Number_Cart_Elm(request):
    try:
        if 'cart' in request.session:
            cart = request.session['cart']
            return JsonResponse({'nbElm':len(cart)})
        else:
            return JsonResponse({'nbElm':0})
    except Exception as e:
        return JsonResponse({'error':str(e)})