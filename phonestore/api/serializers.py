# serializers.py
from rest_framework import serializers

from .models import Phone

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'brand', 'model', 'price', 'img', 'desc')

