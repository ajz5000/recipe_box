from django import forms
from recipe_store.models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        #fields = '__all__'
        exclude = ('ingredients',)
    
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        #fields = '__all__'
        exclude = ('recipe',)


