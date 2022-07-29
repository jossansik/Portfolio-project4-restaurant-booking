import pytz
from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from restaurant_app.forms import (
    BookingForm, MyReservationForm, ReservationForm)
from restaurant_app.models import Reservation
from restaurant_app.services import (
    TimeSlot, get_menus, get_timeslots, make_reservation)


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FoodMenuView(View):
    def get(self, request, *args, **kwargs):
        menus = get_menus(0)  # 0 stands for Menu.TYPE = Dishes

        return render(
            request,
            "menu/food_menu.html",
            {
                "menus": menus,
            },
        )


class DrinksMenuView(View):
    def get(self, request, *args, **kwargs):
        menus = get_menus(1)  # 1 stands for Menu.TYPE = Drinks

        return render(
            request,
            "menu/drinks_menu.html",
            {
                "menus": menus,
            },
        )


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
        guest_fullname = request.POST.get('guest_fullname')

        form['reserved_start_date'].initial = date
        form['num_guests'].initial = num_guests
        form['table_id'].initial = table_id
        form['guest_fullname'].initial = guest_fullname

        timeslot = TimeSlot()
        timeslot.reserved_start_date = date
        timeslot.num_guests = num_guests
        timeslot.table_id = table_id

        try:
            make_reservation(request.user, timeslot.table_id,
                             date, num_guests, guest_fullname)
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

        return redirect(reverse('booking_complete'))


class BookingCompleteView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "booking/complete.html", {},
        )


class MyReservationView(View):
    def get(self, request, *args, **kwargs):
        form = MyReservationForm()
        reservation = {}
        reservation_date = {}
        message = request.GET.get('message')

        if any(Reservation.objects.filter(
                guest=request.user,
                reserved_start_date__gte=datetime.now(tz=pytz.UTC))):
            reservation = Reservation.objects.get(
                guest=request.user,
                reserved_start_date__gte=datetime.now(tz=pytz.UTC))
            form['reservation_id'].initial = reservation.id
            reservation_date = reservation.reserved_start_date

        return render(
            request,
            "my/reservation/index.html",
            {
                "form": form,
                "reservation": reservation,
                "date": reservation_date,
                "message": message,
            },
        )

    def post(self, request, *args, **kwargs):
        reservation_id = request.POST.get("reservation_id")
        reservation = Reservation.objects.get(pk=reservation_id)
        reservation.delete()

        return redirect(reverse('my_reservation') + '?message=success')
