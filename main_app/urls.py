from django.urls import path
from . import views

urlpatterns = [
    # First parameter is our Route. Second parameter 
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index')
]