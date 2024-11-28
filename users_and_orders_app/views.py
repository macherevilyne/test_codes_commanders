from django.shortcuts import render
from rest_framework import viewsets

from users_and_orders_app.serializers import *


def Mainpage(request):
    return render(request, 'main_page.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

