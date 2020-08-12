# recipe_store/urls.py

from django.urls import path
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    #RecipeUpdateView,
    recipe_edit, 
    RecipeDeleteView, 
    RecipeCreateView,
    IngredientListView,
    IngredientCreateView,
    IngredientDetailView,
    IngredientUpdateView,
    IngredientDeleteView,
    PantryListView,
    RecipeIngredientAdd,
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipe/new', RecipeCreateView.as_view(), name='recipe_new'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/edit/add_ingredient', RecipeIngredientAdd.as_view(), name='recipe_ing_add'),
    #path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('ingredients', IngredientListView.as_view(), name='ingredients'),
    path('ingredients/new', IngredientCreateView.as_view(), name='ingredient_new'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail'),
    path('ingredients/<int:pk>/edit/', IngredientUpdateView.as_view(), name='ingredient_edit'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('pantry', PantryListView.as_view(), name='pantry'),
]