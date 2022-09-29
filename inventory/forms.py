from django import forms

from .models import RecipeRequirements




class RecipeRequirementUdate(forms.ModelForm):
        
    class Meta:
        model = RecipeRequirements
        fields = (
            # 'ingredient',
            'quantity',
        )
    