from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('about', views.about, name='about'),
    path('api/getProducts', views.get_products, name='get_products'),
    path('api/getNumberPages', views.get_number_pages, name='get_number_pages'),
    path('api/getProductsByPage/<int:page>/<str:filter>', views.get_products_by_page, name='get_products_by_page'),
    path('<int:id>', views.product, name='product'),
    path('api/addToCart/<int:id>/<str:size>/<int:quantity>', views.add_to_cart, name='add_to_cart'),
    path('api/getNumberCartElm', views.get_Number_Cart_Elm, name='get_Number_Cart_Elm'),
    path('api/getCart', views.get_cart, name='add_to_cart'),
    path('api/removeProductCart/<int:id>', views.delete_from_cart, name='delete_from_cart'),
    path('api/checkStock/<int:id>/<str:size>/<int:quantity>', views.check_stock, name='check_stock'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('order', views.order, name='order'),
    path('api/getHistoricalOrders', views.get_historical_orders, name='get_historical_orders'),
    path('api/getProductsFilter/<int:page>/<str:value>', views.get_products_by_page_filter, name='get_products_by_page_filter'),
]