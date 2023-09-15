from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=10)
    product = models.CharField(max_length=50)