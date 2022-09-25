from django.urls import path #, include
# from core import views as core_views
from . import views



urlpatterns = [
    path("", views.indexView, name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    
    path('table', views.ingredientTable, name='table'),
    path('add_ingredient', views.ingredientAdd, name='add_ingredient'),
    path('add_ingredient/add', views.addrecord, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updateingredient/<int:id>', views.updateIngredient, name='updateingredient'),
    
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/delete', views.MenuItemDel.as_view(), name="menu-item-delete"),
    path('menu/<int:pk>/update-item', views.MenuItemUpdate.as_view(), name='menu-item-update'),
    path('menu-item-create', views.MenuItemCreate.as_view(), name="menu-item-create"),
    
    # path('recipe-requirements/<int:pk>', views.RecipeRequirementsListView.as_view(), name='recipe-requirements'),
    # path('recipe-requirements/<int:pk>', views.RecipeRequirementsDetailView.as_view(), name='recipe-requirements'),
    # path('recipe-requirements/<int:pk>', views.recipe_req, name='recipe-requirements'),
    
    path('recipe-requirements/<int:pk>', views.recipe_requrements_table, name='recipe-requirements'),
    path('recipe-requirements/recipe-requirements-delete/<int:pk>/<int:id>', views.del_req_item, \
        name='recipe-requirements-delete'), 
    path('recipe-requirements-add/<int:pk>', views.RecipeRequirementsCreate.as_view(), name='recipe-requirements-add'),
    path('order/<int:pk>', views.order, name='order'),
    
    # path('revenue', views.revenue, name='revenue'),
    path('report/', views.PurchaseView.as_view(), name='purchase-view'),
    
    # path('accounts/', include('django.contrib.auth.urls')),
]
