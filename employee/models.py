from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    designation = models.CharField(max_length=40)
    salary = models.CharField(max_length=40)

class Leave(models.Model):
    type = models.CharField(max_length=40)
    balance = models.IntegerField()
    from_date = models.IntegerField()
    to_date = models.IntegerField()
    no_of_days = models.IntegerField(default=0)
    reason = models.CharField(max_length=150)
    empid = models.ForeignKey(Employee,on_delete=models.CASCADE)

class LeaveConverseResponses(models.Model):
    sentence = models.CharField(max_length=400)

class ProfileConverseResponses(models.Model):
    sentence = models.CharField(max_length=400)
