from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)
    image=models.URLField(max_length = 200)
    
class ToDo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    completed=models.BooleanField(default=False)
    date_creation=models.DateField(auto_now_add=True)
    date_completion=models.DateField()
    deadline_date=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)