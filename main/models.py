from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    varsity_id = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=20)
    phone = models.CharField(max_length=40)
    email = models.EmailField()









