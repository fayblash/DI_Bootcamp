from django.shortcuts import render
from .info import families,animals

# Create your views here.
def read_json():
	with open('info.json', 'r') as f:
		data = json.load(f)
  		return data

def animal(request,animal_id):
    for 
    return render(request,'animal.html', context ={'animal':animal})

def family(request,fam_id):
    for animal in animals:
        if animal['family']==fam_id:
            # fam=family
    return render(request,'family.html', context= {'fam':fam})
