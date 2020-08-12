from django.db import models
from django.urls import reverse

# Create your models here.
class Unit(models.Model):
    
    # Not sure if I care about what type of measure this is
    #VOLUME = 'VOLUME'
    #MASS = 'MASS'

    #MEASURE_CHOICES = [
    #    (VOLUME, 'Volume'),
    #    (MASS, 'Mass'),
    #]

    name = models.CharField(max_length = 20)
    abbreviation = models.CharField(max_length = 5)
    #measure = models.CharField(max_length = 20, choices = MEASURE_CHOICES, default = VOLUME)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
        #TO-DO
        #return reverse('')

class Ingredient(models.Model):
    
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])  

class PantryItem(models.Model):

    item = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=4)
    units = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

    def get_absolute_url(self):
        pass
        #TO-DO
        #return reverse('')

class Recipe(models.Model):
    
    ITALIAN = 'IT'
    ASIAN = 'AS'
    AMERICAN = 'AM'

    TYPE_CHOICES = [
        (ITALIAN, 'Italian'),
        (ASIAN, 'Asian'),
        (AMERICAN, 'American')
    ]
    
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 20, choices = TYPE_CHOICES, default = AMERICAN)
    servings = models.IntegerField()
    prep_time = models.DecimalField(decimal_places=2, max_digits=5) # TODO - change this to an int to hold minutes
    cook_time = models.DecimalField(decimal_places=2, max_digits=5) # TODO - change this to an int to hold minutes
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    directions = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

class RecipeIngredient(models.Model):
    
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=4)
    units = models.ForeignKey(Unit, on_delete=models.CASCADE)
    style = models.TextField(default="", blank=True)

    def __str__(self):
        return self.recipe.name + ": " + self.ingredient.name

    def get_absolute_url(self):
        pass
        # TODO
        #return reverse('')