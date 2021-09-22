from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    phone = models.CharField(max_length=40)
    email = models.EmailField()

