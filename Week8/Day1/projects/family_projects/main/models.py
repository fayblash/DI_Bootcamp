from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    birth_date = models.DateField(default=datetime.now)
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def person_age(self):
        current_date = date.today()
        current_age = current_date.year-self.birth_date.year
        return f'{current_age}'

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    published_on=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Person,on_delete=models.CASCADE)
    
    