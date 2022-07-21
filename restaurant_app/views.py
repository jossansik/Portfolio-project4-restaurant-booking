from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FoodMenuView(TemplateView):
    template_name = "menu/food_menu.html"


class DrinksMenuView(TemplateView):
    template_name = "menu/drinks_menu.html"
