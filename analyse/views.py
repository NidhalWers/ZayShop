import json
from django.http import JsonResponse
from django.shortcuts import render
from base.models import Order, Product,Footwear,Apparel
from django.contrib.auth.models import User
from datetime import datetime
import pandas as pd

# Create your views here.
def index(request):
    if request.user.is_superuser:
        return render(request, 'analyse/index.html')
    else:
        return render(request, 'base/index.html')

# Utils
def get_7_next_days():
    X=pd.DataFrame()
    X['dates']=pd.date_range(start=datetime.today(),periods=7)
    X['dates']=pd.to_datetime(X['dates'])
    return X

#API

def get_total_order(request):
    products = list(Order.objects.all().values())
    return JsonResponse({'total_order':len(products)})

def get_total_sales(request):
    orders = list(Order.objects.all().values())
    total_sales = 0
    for i in range(len(orders)):
        total_sales += orders[i]['total']
    return JsonResponse({'total_sales':total_sales})

def get_number_products_sold(request):
    try:
        orders = list(Order.objects.all().values())
        number_products_sold = 0
        for i in range(len(orders)):
            orders[i]['products'] = orders[i]['products'].replace("\'", "\"")
            orders[i]['products'] = json.loads(orders[i]['products'])
            for j in range(len(orders[i]['products'])):
                number_products_sold += orders[i]['products'][j]['quantity']
        return JsonResponse({'number_products_sold':number_products_sold})
    except Exception as e:
        print(e)
        return JsonResponse({'error':str(e)})

def get_number_users(request):
    users = list(User.objects.all().values())
    return JsonResponse({'number_users':len(users)})

def get_sales_by_day(request):
    orders = list(Order.objects.all().values())
    dates=[]
    sales=[]
    for i in range(len(orders)):
        orders[i]['products'] = orders[i]['products'].replace("\'", "\"")
        orders[i]['products'] = json.loads(orders[i]['products'])
        for j in range(len(orders[i]['products'])):
            if orders[i]['date'] not in dates:
                dates.append(orders[i]['date'])
                sales.append(orders[i]['products'][j]['quantity'])
            else:
                index = dates.index(orders[i]['date'])
                sales[index] += orders[i]['products'][j]['quantity']

    return JsonResponse({'dates':dates,'sales':sales})
        

def get_sales_repartitions(request):
    apparel=0
    footwear=0
    totalArticle = 0
    orders = list(Order.objects.all().values())
    for i in range(len(orders)):
        orders[i]['products'] = orders[i]['products'].replace("\'", "\"")
        orders[i]['products'] = json.loads(orders[i]['products'])
        for j in range(len(orders[i]['products'])):
            totalArticle += orders[i]['products'][j]['quantity']
            if type(orders[i]['products'][j]['size']) == type(0):
                footwear += orders[i]['products'][j]['quantity']
            else:
                apparel += orders[i]['products'][j]['quantity']

    return JsonResponse({'apparel_nb':apparel,'footwear_nb':footwear,'total_nb':apparel+footwear,'pourcentage_apparel':apparel/(apparel+footwear)*100,'pourcentage_footwear':footwear/(apparel+footwear)*100})

def get_last_5_orders(request):
    orderss = list(Order.objects.all().values())
    orders=[]
    for i in range(0,4):
        try:
            orderss[i]['products'] = orderss[i]['products'].replace("\'", "\"")
            orderss[i]['products'] = json.loads(orderss[i]['products'])
            orderss[i]['products'] = len(orderss[i]['products'])
            orders.append(orderss[i])
        except:
            pass
    return JsonResponse({'orders':orders})

