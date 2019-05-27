from django.db import models

# Create your models here.
class Leave(models.Model):
    type = models.CharField(max_length=40)
    days = models.IntegerField(max_length=10)
    balance = models.IntegerField(max_length=10)
    eid = models.IntegerField(max_length=10)

