from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from django.core.mail import send_mail


class CreateOrder(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        order = OrderSerializer(data=request.data)
        if order.is_valid():
            order.save()
            message = '''
            {}
            Имя: {},
            Телефон: {},
            Комментарий: {},
            Дата: {}
            '''.format(request.POST.get('t'), request.POST.get('name'), request.POST.get('phone'),
                       request.POST.get('text'), request.POST.get('date'))
            send_mail(
                u'Заявка с сайта',
                message,
                'mail@axis-marketing.ru',
                ['marukhelin@gmail.com'],
                fail_silently=False,
            )
            return Response(status=201)
        else:
            return Response(status=400)
