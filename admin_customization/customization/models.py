from django.db import models
from django.db.models import CheckConstraint, Q

GENDER = [
    ('male','Male'),
    ('female','Female'),
    ('transgender','Transgender')
]

class Student(models.Model):
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    address = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    standard = models.IntegerField()
    fathers_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    parent_contact_number = models.BigIntegerField()
    profile_image = models.ImageField(upload_to = 'image/profile', blank=True)
    
    class Meta:
        verbose_name = "Student Detail"
        verbose_name_plural = "Student Details"