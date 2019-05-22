from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
import spacy
class EmployeeView(APIView):
    def get(self, request, format=None):
        users = Employee.objects.all()
        serializer = EmployeeSerializer(users,many=True)
        return Response(serializer.data)

class EmployeeAddView(APIView):
    def post(self, request, format=None):


        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSalView(APIView):
        def post(self,request,format=None):
            nlp = spacy.load('en_core_web_sm')
            serializer = SalarySerializer(data=request.data)

            
            return Response(serializer)