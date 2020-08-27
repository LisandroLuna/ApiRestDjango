from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PhoneSerializer
from .models import Phone


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all().order_by('id')
    serializer_class = PhoneSerializer