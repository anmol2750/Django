from django.db import models

class member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phoneno = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"