from sqlite3 import DatabaseError
from tempfile import TemporaryFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
# Importing parent class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age', 'image']
    # fields = '__all__' # fields line will use all the fields mentioned in models.py file - if we wanted some of the fields then we can write it as a list
# fields = ['name', 'age'] - this will restrict what the end user can create.
    # success_url = '/cats/'

    # We are overriding the definition of form_valid from the parent class CreateView in CatCreate which is the child class.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields =['breed', 'description', 'age']

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# 2nd paramter is the path 3rd paramater is saying render certain data into the 2nd parameter
@login_required
def cats_index(request):
    cats = Cat.objects.filter(user = request.user)  
    return render(request, 'cats/index.html', { 'cats': cats})

@login_required
def cats_detail(request, cat_id):
    # SELECT * FROM main_app_cat WHERE id = cat_id
    cat = Cat.objects.get(id = cat_id)

    # Exclude those toy ids which exist in cat_toys table with the current cat_id
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have})

@login_required
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

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

@login_required
def assoc_toy(request, cat_id, toy_id):

    # Add this toy_id with the cat selected
    Cat.objects.get(id = cat_id).toys.add(toy_id)
    return redirect('detail', cat_id = cat_id)

@login_required
def unassoc_toy(request, cat_id, toy_id):

    # Add this toy_id with the cat selected
    Cat.objects.get(id = cat_id).toys.remove(toy_id)
    return redirect('detail', cat_id = cat_id)

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else: 
            error_message = "Invalid signup - Please try again later"

        # GET
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)