from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username', read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields =  ['items', 'total_price', 'status', 'user'] 
        read_only_fields = ['user'] 
        