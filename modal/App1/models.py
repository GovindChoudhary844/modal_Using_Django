from builtins import map

from django.db import models

# Create your models here.

class Employee(models.Model):
    EmpName = models.CharField(max_length=50)
    EmpSalary = models.IntegerField
    EmpGender = models.CharField(max_length=50)