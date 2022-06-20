from datetime import date, datetime
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
import os 
import math

from base.models import Order, Product,Footwear,Apparel

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

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    else :
        if request.method == "POST":
            totalAmount = 0
            canI = True
            for i in range(len(request.session['cart'])):
                totalAmount += request.session['cart'][i]['price']*request.session['cart'][i]['quantity']
                try:
                    req = check_stock_utils(request.session['cart'][i]['id'],request.session['cart'][i]['size'],request.session['cart'][i]['quantity'])
                    if req=='OK':
                        try:
                            reqSotck = update_stock(request.session['cart'][i]['id'],request.session['cart'][i]['quantity'],request.session['cart'][i]['size'])
                            if reqSotck!='OK':
                                canI = False
                        except Exception as e:
                            return JsonResponse({'error':str(e)})
                except Exception as e:
                    return JsonResponse({'error':str(e)})
            if canI:
                try:
                    order = Order(user = request.user,adress = request.POST['adress'],city = request.POST['city'],zip = request.POST['zipcode'],total = totalAmount,date = datetime.now(),status='Pending',paiement='Credit Card',products = request.session['cart'])
                    order.save()
                    request.session['cart'] = []
                    return render(request, 'base/success.html')
                except Exception as e:
                    return render(request, 'base/checkout.html', {'error':str(e),'status':1})
            
        else:
            return render(request, 'base/checkout.html')

def success(request):
    return render(request, 'base/success.html')

def order(request):
    return render(request, 'base/order.html')

# Utils

def number_pages():
    try:
        products = list(Product.objects.all().values())
        length = len(products)
        return math.ceil(length/12)
    except Exception as e:
        return e

def update_stock(id,quantity,size):
    try:
        product = Apparel.objects.get(id=id)
        if size.lower() == 's':
            product.stocks = product.stocks - quantity
            product.save()
            return 'OK'
        elif size.lower() == 'm':
            product.stockm = product.stockm - quantity
            product.save()
            return 'OK'
        elif size.lower() == 'l':
            product.stockl = product.stockl - quantity
            product.save()
            return 'OK'
        elif size.lower() == 'xl':
            product.stockxl = product.stockxl - quantity
            product.save()
            return 'OK'
        elif size.lower() == 'xxl':
            product.stockxxl = product.stockxxl - quantity
            product.save()
            return 'OK'
        return 'Size not found'
    except:
        try:
            product = Footwear.objects.get(id=id)
            if size == 38:
                product.stock38 = product.stock38 - quantity
                product.save()
                return 'OK'
            if size == 39:
                product.stock39 = product.stock39 - quantity
                product.save()
                return 'OK'
            if size == 40:
                product.stock40 = product.stock40 - quantity
                product.save()
                return 'OK'
            if size == 41:
                product.stock41 = product.stock41 - quantity
                product.save()
                return 'OK'
            if size == 42:
                product.stock42 = product.stock42 - quantity
                product.save()
                return 'OK'
            if size == 43:
                product.stock43 = product.stock43 - quantity
                product.save()
                return 'OK'
            if size == 44:
                product.stock44 = product.stock44 - quantity
                product.save()
                return 'OK'
            if size == 45:
                product.stock45 = product.stock45 - quantity
                product.save()
                return 'OK'
            return 'Size not found'
        except Exception as e:
            print(e)
            return e

def check_stock_utils(id,size,quantity):
    try:
        stockToCheck = 'stock'+size.lower()
        try:
            product = Footwear.objects.get(id=id)
        except:
            try:
                product = Apparel.objects.get(id=id)
            except:
                return 'Product not found'
        if product.__dict__[stockToCheck] >= quantity:
            return 'OK'
        else:
            return 'Not enough stock'
    except Exception as e:
        print(e)
        return e

# API

def get_products(request):
    try:
        products = list(Product.objects.all().values())
        return JsonResponse({'products':products})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def get_products_by_page(request,page,filter):
    try:
        if filter == 'all':
            products = list(Product.objects.all().values()[(page-1)*12:page*12])
        elif filter == 'footwear':
            products = list(Footwear.objects.all().values()[(page-1)*12:page*12])
        elif filter == 'apparel':
            products = list(Apparel.objects.all().values()[(page-1)*12:page*12])
        for i in range(len(products)-1):
            if len(products[i]['productDisplayName']) > 30:
                products[i]['productDisplayName'] = products[i]['productDisplayName'][:20] + '...'
        return JsonResponse({'products':products,'error':0})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def get_products_by_page_filter(request,page,value):
    try:
        products = list(Product.objects.filter(masterCategory=value).values()[(page-1)*12:page*12])
    except:
        try:
            products = list(Product.objects.filter(subCategory=value).values()[(page-1)*12:page*12])
        except:
            try:
                products = list(Product.objects.filter(articleType=value).values()[(page-1)*12:page*12])
            except:
                try:
                    products = list(Product.objects.filter(baseColour=value).values()[(page-1)*12:page*12])
                except:
                    try:
                        products = list(Product.objects.filter(season=value).values()[(page-1)*12:page*12])

                    except:
                        try:
                            products = list(Product.objects.filter(gender=value).values()[(page-1)*12:page*12])
                        except Exception as e:
                            print(e)
                            return JsonResponse({'error':str(e)})

    try:
        for i in range(len(products)-1):
            if len(products[i]['productDisplayName']) > 30:
                products[i]['productDisplayName'] = products[i]['productDisplayName'][:20] + '...'
        print(products)
        return JsonResponse({'products':products,'error':0})
    except Exception as e: 
        print(e)
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

def delete_from_cart(request,id):
    try:
        cart = request.session['cart']
        for i in range(len(cart)):
            if cart[i]['id'] == id:
                cart.pop(i)
                request.session['cart'] = cart
                return JsonResponse({'cart':cart})
        return JsonResponse({'error':'Product not found'})
    except Exception as e:
        return JsonResponse({'error':str(e)})

def check_stock(request,id,size,quantity):
    try:
        stockToCheck = 'stock'+size.lower()
        try:
            product = Footwear.objects.get(id=id)
        except:
            try:
                product = Apparel.objects.get(id=id)
            except:
                return JsonResponse({'error':'Product not found'})
        if product.__dict__[stockToCheck] >= quantity:
            return JsonResponse({'error':0})
        else:
            return JsonResponse({'error':'Not enough stock'})
    except Exception as e:
        print(e)
        return JsonResponse({'error':str(e)})

def get_historical_orders(request):
    try:
        orders = list(Order.objects.filter(user=request.user).values())
        for i in range(len(orders)):
            orders[i]['products'] = orders[i]['products'].replace("\'", "\"")
            orders[i]['products'] = json.loads(orders[i]['products'])
        return JsonResponse({'orders':orders,'number':len(orders)})
    except Exception as e:
        print(e)
        return JsonResponse({'error':str(e)})