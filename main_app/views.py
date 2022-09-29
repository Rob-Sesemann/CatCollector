from sqlite3 import DatabaseError
from tempfile import TemporaryFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
# Importing parent class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

# Create your views here.

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#     Cat('Haku', 'Saigonese-Bobtail', 'Handsome Boy', 4),
#     Cat('Tora', 'Saigonese-Bobtail', 'Greedy Bugger', 4),
#     Cat('Obee', 'Long-Haired', 'Nasty', 5),
# ]
# Defining Classes
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age', 'image']
    # fields = '__all__' # fields line will use all the fields mentioned in models.py file - if we wanted some of the fields then we can write it as a list
# fields = ['name', 'age'] - this will restrict what the end user can create.
    # success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields =['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# 2nd paramter is the path 3rd paramater is saying render certain data into the 2nd parameter
def cats_index(request):
    cats = Cat.objects.all()  
    return render(request, 'cats/index.html', { 'cats': cats})

def cats_detail(request, cat_id):
    # SELECT * FROM main_app_cat WHERE id = cat_id
    cat = Cat.objects.get(id = cat_id)

    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})

def add_feeding(request, cat_id):
    # req.body in Node.js
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id = cat_id)
# ListView - To display all the records from the database
# DetailView - To display a single record from the Database
# CreateView - Used to create instance of a model
# DeleteView - Used to delete a record from the database
# UpdateView - used to update an instance of a model

# Create Operation
# router.get
# router.post

# CUD - Create Update Delete

# CBV's for Toy's CRUD Operations

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, cat_id, toy_id):

    # Add this toy_id with the cat selected
    Cat.objects.get(id = cat_id).toys.add(toy_id)
    return redirect('detail', cat_id = cat_id)

def unassoc_toy(request, cat_id, toy_id):

    # Add this toy_id with the cat selected
    Cat.objects.get(id = cat_id).toys.remove(toy_id)
    return redirect('detail', cat_id = cat_id)