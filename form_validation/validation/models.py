from django.db import models


class User(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = ((Male, 'Male'), (Female, 'Female'),)
 
    username = models.CharField(max_length = 30, blank = False, null = False) 
    email = models.CharField(max_length = 30, blank = False, null = False)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = Male)
    password = models.CharField(max_length = 8, blank = False, null = False)