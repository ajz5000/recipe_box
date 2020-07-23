from django.test import TestCase


from recipe_store.models import Recipe



class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name='Test Recipe',
            type='Test Type', 
            servings='99', 
            prep_time='123.00', 
            cook_time='456.00', 
            directions='Test Directions'
        )

    #MODEL FIELD TESTS
    def test_recipe_content(self):
        recipe=Recipe.objects.get(id=1)
        expected_name = f'{recipe.name}'
        expected_type = f'{recipe.type}'
        expected_servings = f'{recipe.servings}'
        expected_preptime = f'{recipe.prep_time}'
        expected_cooktime = f'{recipe.cook_time}'
        expected_directions = f'{recipe.directions}'

        self.assertEqual(expected_name, 'Test Recipe')
        self.assertEqual(expected_type, 'Test Type')
        self.assertEqual(expected_servings, '99')
        self.assertEqual(expected_preptime, '123.00')
        self.assertEqual(expected_cooktime, '456.00')
        self.assertEqual(expected_directions, 'Test Directions')

        # TODO - Need to test that Ingredients field works

    def test_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual('name', field_label)

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(100, max_length)



    #CUSTOM METHOD TESTS
    def test_object_name_is_name_value(self):
        recipe = Recipe.objects.get(id=1)
        expected_object_name = recipe.name
        self.assertEqual(expected_object_name, str(recipe))

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual('/recipe/1/', recipe.get_absolute_url())
