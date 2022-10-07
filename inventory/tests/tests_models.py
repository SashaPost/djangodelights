from django.test import TestCase

from inventory.models import Ingredient
# Create your tests here.



class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name='Potato', quantity=1.7, unit='lbs', unit_price=0.3)
        
    def test_name_label(self):
        ingredient = Ingredient.objects.get(id=1)
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        
    def test_name_max_length(self):
        ingredient = Ingredient.objects.get(id=1)
        max_length = ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
        
    def test_object_representation(self):
        ingredient = Ingredient.objects.get(id=1)
        expected_object_name = f'{ingredient.name}'
        self.assertEqual(str(ingredient), expected_object_name)