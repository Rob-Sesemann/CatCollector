from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat

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

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# 2nd paramter is the path 3rd paramater is saying render certain data into the 2nd parameter
def cats_index(request):
    cats = Cat.objects.all()  
    return render(request, 'cats/index.html', { 'cats': cats})

