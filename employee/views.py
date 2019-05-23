from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from nltk.tokenize import sent_tokenize
from .serializers import *
from rest_framework.response import Response
from nltk.tokenize import word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
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
            sentence = request.data['sentence'].split()
            pos = nltk.pos_tag(sentence)
            # entities = nltk.ne_chunk(pos)
            patterns = """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
            chunker = nltk.RegexpParser(patterns)
            output = chunker.parse(pos)
            ls = []
            for i in output[0][0]:
                ls.append(i)

            # name = request.data['name']
            # something = Employee.objects.filter(name=name).values()
            # myarr = sent_tokenize(sentence)
            # serializer = SalarySerializer(data=request.data)
            # return Response(c[0] for c in entities)
            return Response(ls)