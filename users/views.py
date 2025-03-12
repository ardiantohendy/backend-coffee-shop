from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    phone_number = request.data.get('phone_number', '')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if password != password2:
        return Response({'Error': 'Password do not match!'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'Error': 'Email already used'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, phone_number=phone_number, password=password)
    return Response({'Message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)  # Gunakan email jika diperlukan
    
    if user is None:
        return Response({'Error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": UserSerializer(user).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)