from rest_framework import serializers
from .models import *


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        exclude = ['image', 'is_active', 'date']
