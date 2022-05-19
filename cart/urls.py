from django.urls import path

from . import views

urlpatterns = [
    path('mycart/', views.mycart, name='mycart'),
]