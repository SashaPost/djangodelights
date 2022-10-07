from django import forms

from .models import RecipeRequirements




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