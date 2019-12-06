from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class Ideas(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        if request.GET.get('is_main') and request.GET.get('is_main') == "1":
            objs = Idea.objects.filter(is_active=True, is_main=True).order_by('-date')
        else:
            objs = Idea.objects.filter(is_active=True).order_by('-date')
        serializer = IdeaSerializer(objs, many=True)
        return Response(serializer.data)