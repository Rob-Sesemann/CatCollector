from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.ImageField(upload_to="main_app/static/uploads/", default="")

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'cat_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1) # B L D