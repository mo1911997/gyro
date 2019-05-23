from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
import nltk
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
            # ls = []
            # for i, j in tokens_tag:
            #     if (j == "JJ"):
            #         ls.append(i)
            return Response(output)
            # name = request.data['name']
            # something = Employee.objects.filter(name=name).values()
            # myarr = sent_tokenize(sentence)
            # serializer = SalarySerializer(data=request.data)
            # return Response(c[0] for c in entities)
