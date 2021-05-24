from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=100,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address=models.CharField(max_length=250)


