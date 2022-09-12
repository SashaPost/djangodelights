
from datetime import datetime
from django.db import models
from django.urls import reverse



# Create your models here.

class Ingredient(models.Model):
    
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0.0)
    
    # unit_choice = [
    #     ("tbsp", "Tablespoon"),
    #     ("lbs", "Pound")
    # ]
    
    def get_absolute_url(self):
        return reverse('ingredients', kwargs={'pk': self.pk})
        
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    
    # contents = None
    
    def get_absolute_url(self):
        return reverse("menu-item", kwargs={"pk": self.pk})
    

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    
    # ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # quantity = models.ForeignKey(to=Ingredient, to_field='quantity', 
                    # on_delete=models.CASCADE, related_name='required_quantity')
    # ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='ingredient_name')
    
    def get_absolute_url(self):
        return reverse("recipe-requirements", kwargs={"pk": self.pk})
    
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now(),
                        blank=None, null=None)
    
    def get_absolute_url(self):
        return reverse("purchase", kwargs={"pk": self.pk})
    
