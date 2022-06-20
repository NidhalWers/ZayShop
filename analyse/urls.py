from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/totalOrder', views.get_total_order, name='get_total_order'),
    path('api/totalSales', views.get_total_sales, name='get_total_sales'),
    path('api/totalProduct', views.get_number_products_sold, name='get_number_products_sold'),
    path('api/totalUser', views.get_number_users, name='get_number_users'),
    path('api/salesRepartition', views.get_sales_repartitions, name='get_sales_repartitions'),
]