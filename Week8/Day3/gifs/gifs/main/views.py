from django.shortcuts import render
from .models import Category,Gif
from .forms import CategoryForm,GifForm

# Create your views here.
def homepage(request):
    gifs=Gif.objects.all()
    return render(request, 'homepage.html', {'gifs':gifs})

def add_category(request):
    if request.method=='GET':
        form=CategoryForm()
        return render(request,'add_new.html',{'form':form,'add_type':'Category'})

    if request.method=='POST':
        form =CategoryForm(request.POST)
        
        if form.is_valid():
            category=Category.objects.create(name=form.cleaned_data['name'])
        
        return redirect('homepage')

def add_gif(request):
    if request.method=='GET':
        form=GifForm()    
        return render(request,'add_new.html',{'form':form,'add_type':'Gif'})

    if request.method=='POST':
        form =GifForm(request.POST)
        if form.is_valid():
            Gif.objects.create(**form.cleaned_data)
        return redirect('homepage')

def single_category(request, category_id):
    category = Category.objects.get(id=category_id)
    # gifs=category.gif_set.all()
    gifs=Gif.objects.filter(categories=category)
    return render(request, 'single_category.html', {'category': category, 'gifs':gifs})

def all_categories(request):
    categories=Category.objects.all()
    return render(request, 'all_categories.html', {'categories':categories})

def gif(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    # gifs=category.gif_set.all()
    categories=Category.objects.filter(gif=gif)
    return render(request, 'gif.html', {'categories': categories, 'gif':gif})
