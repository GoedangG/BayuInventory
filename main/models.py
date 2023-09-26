from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add= True)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    hobby = models.TextField()