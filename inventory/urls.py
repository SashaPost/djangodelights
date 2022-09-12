from django.urls import path
from . import views



urlpatterns = [
    path("", views.indexView, name="index"),
    # path("ingredients", views.IngredientView.as_view(), name="ingredients"),
    path('ingredients', views.IngredientTableView, name='ingredients'),
    path('menu', views.MenuItemView.as_view(), name='menu')
]
