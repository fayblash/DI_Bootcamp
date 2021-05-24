from django.shortcuts import render
from .models import Animal,Family

# Create your views here.

def all_animals(request):
    animals=Animal.objects.all()
    return render(request, 'all_animals.html', {'all_animals':animals})
    
def single_animal(request,animal_id):
    animal=Animal.objects.get(id=animal_id)
    return render(request, 'single_animal.html', {'animal':animal})

    
def single_family(request, family_id):
    fam = Family.objects.get(id=family_id)
    animals=fam.animal_set.all()
    # animals=Animal.objects.filter(family=fam)
    return render(request, 'single_family.html', {'family': fam, 'animals':animals})


    

