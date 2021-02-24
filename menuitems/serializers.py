from rest_framework import serializers

from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'text', 'category', 'description', 'count', 'price') #'__all__'
