from rest_framework import serializers
from .models import *


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        exclude = ['image', 'is_main', 'is_active', 'date']
