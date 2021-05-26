from django import forms
from .models import Category,Gif

class GifForm(forms.Form):
    uploader_name=forms.CharField(max_length=40)
    title=forms.CharField(max_length=100)
    url=forms.CharField(max_length=200)
    categories=forms.ModelMultipleChoiceField(queryset=Category.objects.all())
   
class CategoryForm(forms.Form):
    name=forms.CharField(max_length=40)
