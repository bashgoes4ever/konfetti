# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('reviews/', Reviews.as_view()),
]