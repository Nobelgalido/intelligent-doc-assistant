from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    """API endpoint for user registration"""
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Anyone can register
    serializer_class = UserRegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully',
        }, status=status.HTTP_201_CREATED)
        
class UserProfileView(generics.RetrieveUpdateAPIView):
    """API endpoint to get/update user profile"""
    permission_classes = (IsAuthenticated,) # Must be logged in
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user