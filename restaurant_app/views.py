from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from restaurant_app.forms import BookingForm, ReservationForm
from restaurant_app.services import TimeSlot, get_timeslots, make_reservation


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


class BookingDetailsView(View):
    def get(self, request, *args, **kwargs):
        form = ReservationForm()

        datestr = request.GET.get('time')
        date = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
        num_guests = request.GET.get('num_guests')
        table_id = request.GET.get('table_id')

        form['reserved_start_date'].initial = date
        form['num_guests'].initial = num_guests
        form['table_id'].initial = table_id

        timeslot = TimeSlot()
        timeslot.reserved_start_date = date
        timeslot.num_guests = num_guests
        timeslot.table_id = table_id

        return render(
            request,
            "booking/details.html",
            {
                "form": form,
                "timeslot": timeslot
            },
        )

    def post(self, request, *args, **kwargs):
        form = ReservationForm()

        datestr = request.POST.get('reserved_start_date')
        date = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
        num_guests = request.POST.get('num_guests')
        table_id = request.POST.get('table_id')

        form['reserved_start_date'].initial = date
        form['num_guests'].initial = num_guests
        form['table_id'].initial = table_id

        timeslot = TimeSlot()
        timeslot.reserved_start_date = date
        timeslot.num_guests = num_guests
        timeslot.table_id = table_id

        try:
            make_reservation(request.user, timeslot.table_id, date, num_guests)
        except ValidationError as ex:
            return render(
                request,
                "booking/details.html",
                {
                    "form": form,
                    "timeslot": timeslot,
                    "error": ex.message
                },
            )

        return redirect(reverse('booking_complete') + '?num_guests=' + num_guests + '&date=' + datestr)


class BookingCompleteView(View):
    def get(self, request, *args, **kwargs):
        datestr = request.GET.get('date')
        date = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
        num_guests = request.GET.get('num_guests')

        return render(
            request,
            "booking/complete.html",
            {
                "num_guests": num_guests,
                "date": date
            },
        )
