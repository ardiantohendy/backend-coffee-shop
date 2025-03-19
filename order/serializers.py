from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username', read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.ListField(write_only=True)

    class Meta:
        model = Order
        fields =  ['items', 'total_price', 'status', 'user'] 
        read_only_fields = ['user', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        user = self.context['request'].user
        
        validated_data.pop('user', None) 

        order = Order.objects.create(user=user, **validated_data)
        total_price = 0


        for item_data in items_data:
            menu_item = MenuItem.objects.get(id=item_data['menu_item'])
            quantity = item_data['quantity']
            price = menu_item.price * quantity
            total_price += price

            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

        order.total_price = total_price
        order.save()

        return order
        
        