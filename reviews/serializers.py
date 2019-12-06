from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['image', 'is_active', 'id']
