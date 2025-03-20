from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer, UserSerializer, ProfileUpdateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.


class RegisterView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = self.get_tokens_for_user(user)
            return Response(
                {"user": UserSerializer(user).data, "tokens": tokens},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class LoginApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        tokens = self.get_tokens_for_user(user)

        return Response({"user": UserSerializer(user).data, "tokens": tokens})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class UserProfileView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UpdateProfileView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        
        user = request.user
        
        serializer = ProfileUpdateSerializer(user)
        
        return serializer.data

    def put(self, request):
        
        user = request.user
        
        serializer = ProfileUpdateSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
