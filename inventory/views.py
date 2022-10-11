from django import template
from django.urls import reverse, reverse_lazy
from django.shortcuts import (
    render,  
    get_object_or_404,
    redirect,
) 
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView,
)
from django.views.generic.edit import FormMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import (
    Ingredient,
    MenuItem,
    RecipeRequirements,
    Purchase,
)
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from .forms import RecipeRequirementUdate, RecipeRequirementsAdd

# Create your views here.



@login_required
def indexView(request):
    template_name = 'inventory/index.html'
    return render(request, template_name)
    
@login_required
def ingredientTable(request):
    ingredients = Ingredient.objects.all()
    template = loader.get_template('inventory/one_more_table.html')
    context = {'ingredients': ingredients}
    return HttpResponse(template.render(context, request))

@login_required
def ingredientAdd(request):
    template = loader.get_template('inventory/add_ingredient.html')
    return HttpResponse(template.render({}, request))

@login_required
def addrecord(request):
    new_name = request.POST['name']
    new_quantity = request.POST['quantity']
    new_units = request.POST['units']
    new_unit_price = request.POST['unit_price']
    new_ingredient = Ingredient(name=new_name, quantity=new_quantity,
                                unit=new_units, unit_price=new_unit_price)
    new_ingredient.save()
    return redirect('table')

@login_required
def delete(request, id):
    excluded_ingredient = Ingredient.objects.get(id=id)
    excluded_ingredient.delete()
    return HttpResponseRedirect(reverse('table'))

@login_required
def update(request, id):
    upd_ingredient = Ingredient.objects.get(id=id)
    template = loader.get_template('inventory/ingredient_update.html')
    context = {
        'upd_ingredient': upd_ingredient
        }
    return HttpResponse(template.render(context, request))

@login_required
def updateIngredient(request, id):
    name = request.POST['name']
    quantity = request.POST['quantity']
    unit = request.POST['units']
    unit_price = request.POST['unit_price']
    ingredient = Ingredient.objects.get(id=id)
    ingredient.name = name
    ingredient.quantity = quantity
    ingredient.unit = unit
    ingredient.unit_price = unit_price
    ingredient.save()
    return redirect('table')

    
    
class MenuItemView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu_item'
    
class MenuItemDel(LoginRequiredMixin, DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu')
    
class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    fields = [
        'title',
        'price',
    ]
    template_name = 'inventory/menuitem-update_form.html'
    success_url = ''
    
class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    fields = [
        'title',
        'price',
    ]
    template_name = 'inventory/menuitem-create_form.html'
    success_url = ''
    
    
    
class RecipeRequirementsCreate(LoginRequiredMixin, CreateView):
    
    def get_initial(self, **kwargs):
        initial = super().get_initial()
        initial['menu_item'] = self.kwargs['pk']
        return initial
        
    model = RecipeRequirements
    fields = [
        'menu_item',
        'ingredient',
        'quantity',
    ]
    template_name = 'inventory/recipe_req-add.html'
    success_url = reverse_lazy('menu')
    
    


def split_list(lst, step):
    for i in range(0, len(lst), step):
        yield lst[i:i + step]

@login_required
def recipe_requrements_table(request, pk):
    
    template = loader.get_template('inventory/recipe-req.html')
    given_menu_item = MenuItem.objects.get(id=pk)
    recipe_reqs = RecipeRequirements.objects.all().values()
    
    rows_list = list()
    for item in recipe_reqs:
        if item['menu_item_id'] == pk:
            rows_list.append(Ingredient.objects.get(id=item['ingredient_id']).name) 
            rows_list.append(item['ingredient_id'])
            rows_list.append(Ingredient.objects.get(id=item['ingredient_id']).quantity)
            rows_list.append(item['quantity'])
            rows_list.append(Ingredient.objects.get(id=item['ingredient_id']).quantity // item['quantity'])
            
    list_for_table = list(split_list(rows_list, 5))
    
    context = {
        'given_menu_item': given_menu_item,
        'list_for_table': list_for_table,    
    }
    return HttpResponse(template.render(context, request))



@login_required
def edit_requirement(request, pk, id):
    
    menu_item_id = pk
    ingredient_id = id
    
    menu_item = MenuItem.objects.get(id=menu_item_id)
    ingredient = Ingredient.objects.get(id=ingredient_id)
    ingredient_reqs = Ingredient.objects.get(id=ingredient_id).ingredient_req
    
    for requirement in ingredient_reqs.values():
        if requirement['menu_item_id'] == menu_item_id:
            required_quantity = requirement['quantity']
    if request.method == 'POST':
        form = RecipeRequirementUdate(request.POST)
        if form.is_valid():
            new_req_quantity = request.POST['quantity']
            req_id = int()
            for requirement in menu_item.menu_req.values():
                if requirement['ingredient_id'] == ingredient_id:
                    req_id = requirement['id']
                    upd_req = RecipeRequirements.objects.get(id=req_id)
                    upd_req.quantity = new_req_quantity
                    upd_req.save()
            return redirect('recipe-requirements', pk=menu_item_id)
    else:
        form = RecipeRequirementUdate()
    
    context = {
        'menu_item_id': menu_item_id,
        'ingredient_id': ingredient_id,
        
        'ingredient': ingredient,
        'menu_item': menu_item,
        
        'form': form,
        'required_quantity': required_quantity,
    }
    return render(request, 'inventory/recipe-req-update.html', context)
    


@login_required
def order(request, pk):
    menu_item = MenuItem.objects.get(id=pk)
    requirements = menu_item.menu_req.all()
    purchase = Purchase(menu_item=menu_item)
    
    for requirement in requirements:
        req_ingredient = requirement.ingredient
        req_ingredient.quantity -= requirement.quantity
        req_ingredient.save()
    purchase.save()
    
    return redirect('menu')


    
    
@login_required
def del_req_item(request, pk, id):
    menu_item_id = pk
    ingredient_id = id
    menu_item = MenuItem.objects.get(id=menu_item_id)
    menu_item_requirements = menu_item.menu_req
    
    for requirement in menu_item_requirements.values():
        if requirement['ingredient_id'] == ingredient_id:
            req = RecipeRequirements.objects.get(id=requirement['id'])
            req.delete()
    
    return redirect('recipe-requirements', pk=pk)




class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    
    def revenue(self):
        dirty_income = 0
        menu_ingredients_price = 0
        all_purchases = Purchase.objects.all().values()
        for purchase in all_purchases:
            menu_item = MenuItem.objects.get(id=purchase['menu_item_id'])
            dirty_income += menu_item.price       
            menu_reqs = menu_item.menu_req.all()
            for req in menu_reqs:
                menu_ingredients_price += (Ingredient.objects.get(name=req.ingredient).unit_price * req.quantity)
        profit = dirty_income - menu_ingredients_price
        return {
            'dirty_income': dirty_income,
            'menu_ingredients_price': menu_ingredients_price,
            'profit': profit,
        }
       
    def get_context_data(self, **kwargs):
        context = super(PurchaseView, self).get_context_data(**kwargs)
        context['all_purchases'] = Purchase.objects.all()
        context['revenue'] = self.revenue
        return context
    
    
    

@login_required
def log_out(request):
    logout(request)
    return redirect("/")
