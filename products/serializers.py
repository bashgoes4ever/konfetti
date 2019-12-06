from rest_framework import serializers
from .models import *


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class CategoriesIndexSerializer(serializers.ModelSerializer):
    section = SectionSerializer()
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image_thumb', 'section']


class ChildCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoriesSerializer(serializers.ModelSerializer):
    section = SectionSerializer()
    children = ChildCategoriesSerializer(many=True)
    class Meta:
        model = Category
        exclude = ['image', 'image_thumb', 'is_main', 'parent', 'title', 'description']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'image_thumb']
