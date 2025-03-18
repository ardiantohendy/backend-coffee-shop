from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



