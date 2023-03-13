from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    course = models.CharField(max_length=50, default='computerscience', blank=False)
    year = models.CharField(max_length=50, default='', blank=False)
    gender = models.CharField(max_length=50, blank=False, null=False)


def __str__(self):
    return self.name

