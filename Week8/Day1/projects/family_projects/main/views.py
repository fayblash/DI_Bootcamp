from django.shortcuts import render
from datetime import datetime
from .model import Person,Post

# Create your views here.
def homepage(request):
    # name='Fay'
    people=Person.objects.all()
    # today=datetime.now()
    return render(request, 'homepage.html',
        {'persons':people})

def my_posts(request,person_id):
    person=Person.objects.get(id=person_id)
    return render(request, 'myposts.html')
    
def about(request, name):
    return render(request,'about.html',
        {'name':name})

