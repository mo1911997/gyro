from rest_framework import serializers
from .models import Employee,Leave,LeaveConverseResponses,ProfileConverseResponses
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = "__all__"

class Employee2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["salary"]

class LeaveConSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveConverseResponses
        fields = "__all__"

class ProfileConSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileConverseResponses
        fields = ['sentence']