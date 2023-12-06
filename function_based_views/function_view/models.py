from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name