from django import forms

from .models import MenuItem, RecipeRequirements



class MenuItemCreateForm(forms.ModelForm):
    
    class Meta:
        model = MenuItem
        fields = (
            'title',
            'price',
        )



class RecipeRequirementUdate(forms.ModelForm):
        
    class Meta:
        model = RecipeRequirements
        fields = (
            'quantity',
        )
    


class RecipeRequirementsAdd(forms.ModelForm):
    
    class Meta:
        model = RecipeRequirements
        fields = (
            'menu_item',
            'ingredient',
            'quantity',
        )