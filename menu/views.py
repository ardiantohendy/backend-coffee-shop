from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

@api_view(['GET'])
def get_data(request):
    menu = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu, many=True, context={'request': request})
    return Response(serializer.data)