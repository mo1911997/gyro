from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Employee
from django.shortcuts import redirect,render
from rest_framework import status
import json
import sys
import re
import requests
from .serializers import *
from rest_framework.response import Response
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk
from nltk import pos_tag
from nltk import RegexpParser
from nltk import word_tokenize

iid = -1
flag = 0
list1 = []

class EmployeeView(APIView):
    def get(self, request, format=None):
        users = Employee.objects.all()
        serializer = EmployeeSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaveView(APIView):
    def post(self, request, format=None):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        users = Leave.objects.all()
        serializer = LeaveSerializer(users, many=True)
        list = serializer.data
        return Response(list)

    def delete(self, request, format=None):
        users = Leave.objects.all()
        users.delete()
        return Response("done")

class GetOneEmployeeView(APIView):
    def post(self, request, format=None):
        global flag
        user_id = request.data['id']
        user = Employee.objects.filter(id=user_id)
        serializer = EmployeeSerializer(user, many=True)
        flag = 0
        return Response(serializer.data)

class GetSalView(APIView):
    def post(self,request,format=None):
        global flag
        user_id = request.data['id']
        user = Employee.objects.filter(id=user_id)
        serializer = Employee2Serializer(user, many=True)
        flag = 0
        return Response(serializer.data)

class MainView(APIView):

    def post(self,request,format=None):
        sentence = request.data['sentence']
        id = request.data['id']
        global list1
        list1.append(sentence)
        global flag
        r = None
        if (flag == 0):
            entity_extraction(sentence)
        if (flag == 1):
            r = requests.get('https://peaceful-shore-77889.herokuapp.com/employee/getleaveconv/')
            s = "thank you"
            result = re.search(s, r.text)
            if (result):
                d = {}
                d['type'] = list1[1]
                d['days'] = list1[2]
                d['fromdate'] = list1[3]
                d['todate'] = list1[4]
                d['reason'] = list1[5]
                d['empid'] = id
                list1.clear()
                r = requests.post('https://peaceful-shore-77889.herokuapp.com/employee/leave/', data=d)
        elif (flag == 2):
            r = requests.post('https://peaceful-shore-77889.herokuapp.com/employee/getemp/', data = request.data)
        elif (flag == 3):
            r = requests.post('https://peaceful-shore-77889.herokuapp.com/employee/getsal/', data = request.data)
        elif (flag == 4):
            r = requests.get('https://peaceful-shore-77889.herokuapp.com/employee/getprofileconv/')
            s = "thank you"
            result = re.search(s, r.text)
            if (result):
                d = {}
                d['name'] = list1[1]
                d['phone'] = list1[2]
                d['email'] = list1[3]
                d['designation'] = list1[4]
                d['salary'] = list1[5]
                list1.clear()
                r = requests.post('https://peaceful-shore-77889.herokuapp.com/employee/', data = d)
        else:
            print("bo...")

        return Response(r)

class LeaveApply(APIView):

    def post(self,request,format=None):
        serializer = LeaveConSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        # try:
        #     global iid,flag
        #     iid = iid + 1
        #     users = LeaveConverseResponses.objects.all()
        #     serializer = LeaveConSerializer(users, many=True)
        #     list = serializer.data
        #
        #     return Response(list)
        # except IndexError:
        #     iid = -1
        #     flag = 0
        #     return Response("thank you")
        users = LeaveConverseResponses.objects.all()
        serializer = LeaveConSerializer(users, many=True)
        return Response(users)

class ProfileApply(APIView):

    def post(self,request,format=None):
        serializer = ProfileConSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        try:
            global iid,flag
            iid = iid + 1
            users = ProfileConverseResponses.objects.all()
            serializer = ProfileConSerializer(users, many=True)
            list = serializer.data
            return Response(list[iid])
        except IndexError:
            iid = -1
            flag = 0
            return Response("thank you")



def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield ' '.join(word for word, tag in subtree.leaves())

def entity_extraction(sentence):
    global flag
    tokens_tag = word_tokenize(sentence)
    poss_tag = pos_tag(tokens_tag)
    #grammar = "NP: {<VBP>*<VB>*<IN>?<DT>?<NN>}"
    grammar = "NP: {<VB>?<IN>?<DT>?<JJ>?<NN>?}"
    # grammar = "NP: {<DT|PP\$>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(poss_tag)
    result2 = extract_np(result)
    for npstr in result2:
        if (npstr == "apply for leave"):
            flag = 1
        elif (npstr == "details"):
            flag = 2
        elif (npstr == "salary"):
            flag = 3
        elif (npstr == "profile"):
            flag = 4
        else:
            print("yo...")

class Demo(APIView):
    def get(self,request,format=None):
            return Response(request.data)
