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
    days = models.IntegerField(max_length=10)
    balance = models.IntegerField(max_length=10)
    empid = models.ForeignKey(Employee,on_delete=models.CASCADE)
