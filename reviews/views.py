from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from time import sleep


class Reviews(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        objs = Review.objects.filter(is_active=True)
        serializer = ReviewSerializer(objs, many=True)
        return Response(serializer.data)