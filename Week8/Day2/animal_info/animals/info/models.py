from django.db import models

# Create your models here.
class Family(models.Model):
    name=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Animal(models.Model):
    name=models.CharField(max_length=40)
    legs=models.IntegerField()
    weight=models.FloatField()
    height=models.FloatField()
    speed=models.FloatField()
    family=models.ForeignKey('Family', on_delete=models.CASCADE)
    
class AnimalClimate(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    
    CHOICES=[
        ('a','Arid'),
        ('d','Desert'),
        ('s','Swamp')
    ]
class Country(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    country_of_origin=models.ForeignKey(Country,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Passport(models.Model):
    person=models.OneToOneField(Person,on_delete=models.CASCADE)
    pass_id=models.CharField(max_length=10)
    visited_countries=models.ManyToManyField(Country)

    def __str__(self):
        return f'Passport ID {self.pass_id} for {self.person}'

class BankAccount(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='bankaccounts')
    account_id=models.CharField(max_length=10)



