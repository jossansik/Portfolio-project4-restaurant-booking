from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from restaurant_app.forms import BookingForm
from restaurant_app.services import get_timeslots


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FoodMenuView(TemplateView):
    template_name = "menu/food_menu.html"


class DrinksMenuView(TemplateView):
    template_name = "menu/drinks_menu.html"


class BookingView(View):
    def get(self, request, *args, **kwargs):
        form = BookingForm()

        return render(
            request,
            "booking/index.html",
            {
                "form": form,
            },
        )

    def post(self, request, *args, **kwargs):
        num_guests = request.POST.get('num_guests')
        datestr = request.POST.get('reserved_start_date')

        date = datetime.strptime(datestr, "%Y-%m-%d").date()

        timeslots = get_timeslots(num_guests, date)

        return render(
            request,
            "booking/index.html",
            {
                "timeslots": timeslots,
            },
        )
