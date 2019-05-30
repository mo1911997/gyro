from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
import json
from urllib.request import urlopen
import requests
from .serializers import *
from rest_framework.response import Response
import nltk
id = 0
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

class GetEmployeeLeaveView(APIView):
    def post(self, request, format=None):
        user_id = request.data['empid']
        user = Leave.objects.filter(empid=user_id)
        serializer = Leave2Serializer(user, many=True)
        return Response(serializer.data)

class GetSalView(APIView):
        def post(self,request,format=None):
            # sentence = word_tokenize(request.data['sentence'])
            sentence = request.data['sentence']
            empid = request.data['empid']
            tokens_tag = pos_tag(word_tokenize(sentence))
            output = ne_chunk(tokens_tag)
            r = None
            salary_param = []
            for i, j in tokens_tag:
                 if (j == "NN" or j =="JJ"):
                     salary_param.append(i)
                     r = requests.post('https://peaceful-shore-77889.herokuapp.com/employee/getempleave/',data = request.data)
                     #ss = json.load(salary_param)
            return Response(r)
            # name = request.data['name']
            # something = Employee.objects.filter(name=name).values()
            # myarr = sent_tokenize(sentenc/e)
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
    def get(self,request,format=None):
        users = Leave.objects.all()
        serializer = LeaveSerializer(users, many=True)
        list = []
        list = serializer.data
        return Response(list[0])

    def post(self,request,format=None):
        sentence = request.data['sentence']
        r = requests.get('https://peaceful-shore-77889.herokuapp.com/employee/getleaveconv/')
        return Response(r)

class LeaveApply(APIView):
    def post(self,request,format=None):
        serializer = LeaveConSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        try:

            global id
            id+=1
            users = LeaveConverseResponses.objects.all()
            serializer = LeaveConSerializer(users, many=True)
            list = []
            list = serializer.data
            length = len(list)
        except:
            id = 0
            return Response("thank you")
        return Response(list[id])







