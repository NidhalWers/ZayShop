from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('api/getProducts', views.get_products, name='get_products'),
    path('api/getNumberPages', views.get_number_pages, name='get_number_pages'),
    path('api/getProductsByPage/<int:page>', views.get_products_by_page, name='get_products_by_page'),
    path('<int:id>', views.product, name='product'),
    path('api/addToCart/<int:id>/<str:size>/<int:quantity>', views.add_to_cart, name='add_to_cart'),
    path('api/getNumberCartElm', views.get_Number_Cart_Elm, name='get_Number_Cart_Elm'),
    path('api/getCart', views.get_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
]