from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='about'),
    path('shopping/', views.ShoppingPage, name='shopping'),
    path('gaming/', views.gaming_store, name='gaming'),
]
