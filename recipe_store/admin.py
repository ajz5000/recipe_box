from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Unit, PantryItem

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Unit)
admin.site.register(PantryItem)