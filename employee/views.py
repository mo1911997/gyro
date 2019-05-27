from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
import json
from urllib.request import urlopen
from requests import request
from .serializers import *
from rest_framework.response import Response
import nltk

import urllib.parse

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk
from nltk import pos_tag
from nltk import word_tokenize
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
            # sentence = word_tokenize(request.data['sentence'])
            sentence = request.data['sentence']
            tokens_tag = pos_tag(word_tokenize(sentence))
            output = ne_chunk(tokens_tag)
            salary_param = []
            for i, j in tokens_tag:
                 if (j == "NN" or j =="JJ"):
                     salary_param.append(i)
                     #ss = json.load(salary_param)
            return Response(salary_param)
            # name = request.data['name']
            # something = Employee.objects.filter(name=name).values()
            # myarr = sent_tokenize(sentence)
            # serializer = SalarySerializer(data=request.data)
            # return Response(c[0] for c in entities)

class LeaveAddView(APIView):
    def post(self, request, format=None):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaveView(APIView):
    # def post(self, request, format=None):
    #     user_id = request.data['id']
    #     user = Leave.objects.filter(id=user_id)
    #     #users = Leave.objects.all()
    #     serializer = LeaveSerializer(user, many=True)
    #     return Response(serializer.data)

    def post(self,request,format=None):
        type = request.data['type']
        days = request.data['days']
        balance = request.data['balance']
        empid  = request.data['empid']

        post_data = [('type',type),('days',days),('balance',balance),('empid',empid)]

        result =urllib.request.urlopen("https://peaceful-shore-77889.herokuapp.com/employee/addleave/",urllib.parse.urlencode(post_data))
        content =result.read()
        return Response(content)