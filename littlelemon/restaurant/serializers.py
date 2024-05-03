from rest_framework import serializers # type: ignore
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BookingTable
        fields = '__all__'
