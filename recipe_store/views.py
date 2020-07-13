#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipe_new.html'
    #need to add Ingredients to fields once I understand how the selection should work
    fields = ['name', 'type', 'servings', 'prep_time', 'cook_time', 'directions']

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipe_edit.html'
    #need to add Ingredients to fields once I understand how the selection should work
    fields = ['name', 'type', 'servings', 'prep_time', 'cook_time', 'directions']

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('home')
