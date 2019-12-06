from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class Sales(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        objs = Sale.objects.filter(is_active=True).order_by('-date')
        serializer = SaleSerializer(objs, many=True)
        return Response(serializer.data)