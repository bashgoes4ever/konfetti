from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('ideas.urls')),
    path('api/v1/', include('sales.urls')),
    path('api/v1/', include('contacts.urls')),
    path('api/v1/', include('order.urls')),
]

urlpatterns += [re_path(r'^.*',  include("start.urls"))]