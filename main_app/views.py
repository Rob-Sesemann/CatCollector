from sqlite3 import DatabaseError
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
# Importing parent class
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    return render(request, 'cats/detail.html', {'cat': cat})

# ListView - To display all the records from the database
# DetailView - To display a single record from the Database
# CreateView - Used to create instance of a model
# DeleteView - Used to delete a record from the database
# UpdateView - used to update an instance of a model

# Create Operation
# router.get
# router.post

# CUD - Create Update Delete

