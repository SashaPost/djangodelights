
# from datetime import datetime
from django.utils import timezone
from django.db import models
from django.urls import reverse


now = timezone.now
# Create your models here.

class Ingredient(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0.0)
    
    def get_absolute_url(self):
        return reverse('ingredients', kwargs={'pk': self.pk})
    
        
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['quantity']
        
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    
    def get_absolute_url(self):
    #     return reverse("menu-item", kwargs={"pk": self.pk})
        return reverse("menu")
    
    def __str__(self):
        return f'{self.title}'
    
    def available(self):
        return all(item.enough() for item in self.menu_req.all())
    

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='menu_req', on_delete=models.CASCADE, db_constraint=False)
    ingredient = models.ForeignKey(Ingredient, related_name='ingredient_req', on_delete=models.CASCADE, db_constraint=False)
    quantity = models.FloatField(default=0.0)
    
    def get_absolute_url(self):
        return reverse("recipe-requirements", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.menu_item}, {self.ingredient}, {self.quantity}'
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
    def not_null(self):
        if self.quantity == 0.0:
            return False
        else:
            return True
    
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='menu_purchase', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now,
                        blank=None, null=None)
    
    def get_absolute_url(self):
        return reverse("purchase", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.menu_item}'
    
    class Meta:
        ordering = ['-timestamp']
    
