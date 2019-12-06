from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class ContactsView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        objs = Contacts.objects.all()[0]
        serializer = ContactsSerializer(objs, many=False)
        return Response(serializer.data)
