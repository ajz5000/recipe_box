from django.test import TestCase
from django.urls import reverse

from recipe_store.models import Recipe, RecipeIngredient, Ingredient, Unit



class HomePageViewTest(TestCase):

    def setUp(self):
        Recipe.objects.create(
            name='Test Recipe',
            type='Test Type',
            servings='99',
            prep_time='123.00',
            cook_time='456.00',
            directions='Test Directions'
        )

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class RecipeDetailViewTest(TestCase):
    
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            type='Test Type',
            servings='99',
            prep_time='123.00',
            cook_time='456.00',
            directions='Test Directions'
        )

        # self.ingredient = Ingredient.objects.create(
        #     name='Test Ingredient'
        # )

        # self.unit = Unit.objects.create(
        #     name='Test Unit',
        #     abbreviation='Test Abbreviation'
        # )

        # RecipeIngredient.objects.create(
        #     quantity='123',
        #     units=self.unit,
        #     recipe=self.recipe,
        #     ingredient=self.ingredient,
        #     style='Test Style'
        # )


    def test_view_url_exists_at_proper_location(self):
        response = self.client.get(self.recipe.get_absolute_url())
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(self.recipe.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_view_content_correct(self):
        response = self.client.get(self.recipe.get_absolute_url())
        self.assertContains(response, 'Test Recipe')

