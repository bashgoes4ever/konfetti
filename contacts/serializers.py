from rest_framework import serializers
from .models import *


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        exclude = ['id']
