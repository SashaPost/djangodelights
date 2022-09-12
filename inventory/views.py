from re import template
from django.urls import reverse
from django.shortcuts import (
    render,  
    get_object_or_404
) 
from django.http import Http404, HttpResponse
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView,
)
from django.views.generic.base import TemplateView
from .models import (
    Ingredient,
    MenuItem,
    RecipeRequirements,
    Purchase,
)
# Create your views here.



def indexView(request):
    # if request.method == 'GET':
    template_name = 'inventory/index.html'
    # return HttpResponse(template_name)
    return render(request, template_name)
    


# class IngredientView(ListView):
#     model = Ingredient
#     template_name = 'inventory/ingredients.html'
    
#     def get_something(self):
#         return Ingredient.objects.all()

def IngredientTableView(request):
    table_data = Ingredient.objects.all()
    return render(request, 'inventory/ingredients_table.html', locals())     

  
    
class MenuItemView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    
    def view_menu(self):
        return MenuItem.objects.all()
    
    
