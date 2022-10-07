from django.test import TestCase
from django.urls import reverse

from inventory.models import Ingredient
# Create your tests here.



class ingredientTableTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        number_of_ingredients = 13
        
        for ingredient_id in range(number_of_ingredients):
            Ingredient.objects.create(
                name=f'Ingredient {ingredient_id}',
                quantity=0.1 + 0.1 * ingredient_id,
                unit='lbs',
                unit_price=0.2 + 0.1 * ingredient_id
            )
        
        
    