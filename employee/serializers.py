from rest_framework import serializers
from .models import Employee,Leave,LeaveConverseResponses
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = "__all__"

class Leave2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ["type","balance"]

class LeaveConSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveConverseResponses
        fields = ["sentence"]