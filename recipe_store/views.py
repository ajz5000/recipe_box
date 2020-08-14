from recipe_store.models import Recipe, RecipeIngredient
from recipe_store.forms import RecipeForm, RecipeIngredientForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Recipe, RecipeIngredient, Ingredient, PantryItem


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

# TODO - consider changing this to a function based view
class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipe_new.html'
    #need to add Ingredients to fields once I understand how the selection should work
    fields = ['name', 'type', 'servings', 'prep_time', 'cook_time', 'directions']

# Attempt at a function based view for editing recipes, this can be modified into a funciton that handles both adding new recipes and editing existing recipes in the future.
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = RecipeIngredient.objects.all().filter(recipe_id=pk)
    if request.method == "POST":
        r_form = RecipeForm(request.POST, instance=recipe)
        ri_forms = [RecipeIngredientForm(request.POST, prefix=str(x), instance=ingredients[x]) for x in range(len(ingredients))]

        if r_form.is_valid() and all([ri_form.is_valid() for ri_form in ri_forms]):
            #recipe = r_form.save(commit=False)
            recipe = r_form.save()
            
            # TODO - WORK ON RECIPEINGREDIENT PROCESSING
            for ri_form in ri_forms:
                ri_form.save()

            return HttpResponseRedirect(recipe.get_absolute_url())#, pk=recipe.pk)

           
    else:
        r_form = RecipeForm(instance=recipe)
        ri_forms = [RecipeIngredientForm(prefix=str(x), instance=ingredients[x]) for x in range(len(ingredients))]
    # DEBUG
    #import pdb; pdb.set_trace()
    return render(request, 'recipe_edit.html', {'recipe_form': r_form, 'recipeingredient_forms': ri_forms})

# Trying out a function based view to handle recipe updates
# class RecipeUpdateView(UpdateView):
#     model = Recipe
#     template_name = 'recipe_edit.html'
#     #need to add Ingredients to fields once I understand how the selection should work
#     fields = ['name', 'type', 'servings', 'prep_time', 'cook_time', 'directions']

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('home')

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients.html'
    context_object_name = 'ingredients'

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "ingredient_new.html"
    fields = ['name',]

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "ingredient_detail.html"

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'ingredient_edit.html'
    fields = ['name',]

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient_delete.html'
    success_url = reverse_lazy('ingredients')

class PantryListView(ListView):
    model = PantryItem
    template_name = 'pantry.html'
    fields = ['item', 'quantity', 'units',]
    context_object_name = 'pantry_items'

class RecipeIngredientAdd(CreateView):
    model = RecipeIngredient
    template_name = 'recipe_ing_add.html'
    fields = ['ingredient', 'quantity', 'units', 'style',]

