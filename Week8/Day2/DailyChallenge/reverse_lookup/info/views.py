from django.shortcuts import render
from .models import Person

# Create your views here.
def phone(request,phone):
    person=Person.objects.get(phone=phone)
    return render(request, 'phone.html', {'person':person})

def name(request,name):
    person=Person.objects.get(name=name)
    return render(request, 'name.html', {'person':person})
    
