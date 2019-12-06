# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    #path('food_type/<str:slug>', FoodTypeSingle.as_view(), name='food_type_single'),
    path('categories/index/', CategoriesIndex.as_view()),
    path('categories/', Categories.as_view()),
    path('products/', Products.as_view()),
]