from django.shortcuts import render
from django.http import JsonResponse
from user.models import User
from user.serializer import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated


# JWT Token View
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# User Registration View
class RegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


# Get All Available Routes
@api_view(['GET'])
def getRoutes(request):
    """
    Returns all available API routes.
    """
    routes = [
        {'path': '/api/token/', 'description': 'Obtain JWT token'},
        {'path': '/api/register/', 'description': 'Register a new user'},
        {'path': '/api/token/refresh/', 'description': 'Refresh JWT token'},
        {'path': '/api/test/', 'description': 'Test endpoint with GET and POST (requires authentication)'},
    ]
    return Response(routes, status=status.HTTP_200_OK)


# Test Endpoint
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    """
    Example endpoint to test API responses.
    """
    if request.method == 'GET':
        data = f"Congratulations {request.user}, your API just responded to a GET request."
        return Response({'response': data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        text = request.data.get('text', 'Hello buddy')
        data = f"Congratulations! Your API just responded to a POST request with text: {text}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
