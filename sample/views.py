from django.shortcuts import render
from rest_framework.views import APIView
from .models import Users
from .serializers import *
from rest_framework.response import Response
# Create your views here.
class UserView(APIView):
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UsersSerializer(users,many=True)
        return Response(serializer.data)