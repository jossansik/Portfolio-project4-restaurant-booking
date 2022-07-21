from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/foodmenu/', views.FoodMenuView.as_view(), name='food_menu'),
    path('menu/drinksmenu/', views.DrinksMenuView.as_view(), name='drinks_menu'),
    path('about/', views.AboutView.as_view(), name='about'),
]