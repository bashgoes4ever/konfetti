from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from django.core.paginator import Paginator
from time import sleep

class Categories(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        if request.GET.get('section'):
            objs = Category.objects.filter(level=0, section__slug=request.GET.get('section'))
        else:
            objs = Category.objects.filter(level=0)
        serializer = CategoriesSerializer(objs, many=True)
        return Response(serializer.data)


class CategoriesIndex(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        objs = Category.objects.filter(is_main=True)
        serializer = CategoriesIndexSerializer(objs, many=True)
        return Response(serializer.data)


class Products(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        options = {}
        if request.GET.get('category'):
            options['category'] = request.GET.get('category')
        if request.GET.get('is_main') and request.GET.get('is_main') == "1":
            options['is_main'] = True
        if request.GET.get('is_top') and request.GET.get('is_top') == "1":
            options['is_top'] = True
        objs = Product.objects.filter(is_active=True, **options).order_by('-date')

        if request.GET.get('is_paginated') and request.GET.get('is_paginated') == "1":
            paginator = Paginator(objs, 9)
            page_num = request.GET.get('page', 1)
            objs = paginator.get_page(page_num)
            is_paginated = objs.has_other_pages()
            serializer = ProductsSerializer(objs, many=True)
            page_next = objs.next_page_number() if objs.has_next() else 'end'
            return Response({
                'data': serializer.data,
                'next_page': page_next
            })

        serializer = ProductsSerializer(objs, many=True)
        return Response(serializer.data)