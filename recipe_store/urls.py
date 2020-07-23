# recipe_store/urls.py

from django.urls import path
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    #RecipeUpdateView,
    recipe_edit, 
    RecipeDeleteView, 
    RecipeCreateView,
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipe/new', RecipeCreateView.as_view(), name='recipe_new'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    #path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
]