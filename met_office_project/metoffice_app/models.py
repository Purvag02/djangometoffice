# models.py
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

class Parameter(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    name = models.CharField(max_length=100)
