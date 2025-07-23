# DjangoVueConnection/backend/models.py

""" Models for the backend app """

from django.db import models


class Dog(models.Model):
   """
   Model for a dog
   """
   name = models.CharField(max_length=255)
   age = models.IntegerField()
   color = models.CharField(max_length=255)
   size = models.CharField(max_length=50)


   def __str__(self):
       return self.name
