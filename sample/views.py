from django.shortcuts import render
from rest_framework.views import APIView
from .models import Users
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
# Create your views here.
class UserView(APIView):
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UsersSerializer(users,many=True)
        return Response(serializer.data)

class UserAddView(APIView):
    def post(self, request, format=None):

        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
