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
        read_only_fields = ['user', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        user = self.context['request'].user 

        order = Order.objects.get(id=item_data['menu_item'])
        
        