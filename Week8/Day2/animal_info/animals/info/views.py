from django.shortcuts import render,redirect
from .models import Animal,Family, Person,Country,Passport,BankAccount
from .forms import AnimalForm, FamilyForm, PersonForm,PassportForm

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

def add_animal(request):
    if request.method=='GET':
        return render(request,'create_page.html',{'form':AnimalForm(),'add_type':'Animal'} )
    
    elif request.method=='POST':
        data=request.POST
        form=AnimalForm(data)
        if form.is_valid():    
            animal=Animal.objects.create(**form.cleaned_data)
                # name=form.cleaned_data['name']
                # legs=form.cleaned_data['legs'],
                # weight=form.cleaned_data['weight'],
                # height=form.cleaned_data['height'],
                # speed=form.cleaned_data['speed'],
                # family=form.cleaned_data['family'])
        return redirect('all_animals')
    
def add_family(request):
    if request.method=='GET':
        form=FamilyForm()
        
        return render(request,'create_page.html',{'form':form,'add_type':'Family'})

    if request.method=='POST':
        form =FamilyForm(request.POST)
        
        if form.is_valid():
            fam=Family.objects.create(name=form.cleaned_data['name'])
        
        return redirect('single_family', fam.id)

def add_person(request):
    if request.method=='GET':
        form=PersonForm()    
        return render(request,'create_page.html',{'form':form,'add_type':'Person'})

    if request.method=='POST':
        form =PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(**form.cleaned_data)
        return redirect('add_person')

def add_passport(request):
    if request.method=='GET':
        form=PassportForm()    
        return render(request,'create_page.html',{'form':form,'add_type':'Passport'})

    if request.method=='POST':
        form =PassportForm(request.POST)
        if form.is_valid():
            Passport.objects.create(**form.cleaned_data)
        return redirect('add_passport')
    