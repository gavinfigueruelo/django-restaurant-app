from rest_framework import serializers

from .models import Menu
from .models import Order

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'text', 'category', 'description', 'count', 'price') #'__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
