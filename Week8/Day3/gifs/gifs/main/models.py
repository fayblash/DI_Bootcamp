from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class Gif(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField(max_length = 200)
    uploader_name=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)
    categories=models.ManyToManyField('Category')
    
    def __str__(self):
        return self.title

    

