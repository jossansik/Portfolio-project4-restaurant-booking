from django.forms import ValidationError
from restaurant_app.models import Reservation
from datetime import timedelta, datetime


class TimeSlot:
    def __init__(self):
        self.time = 0,
        self.is_reserved = False,


def make_reservation(user, table, reservation_start_date, num_guests):
    end_date = reservation_start_date + timedelta(minutes=30)
    existingReservation = Reservation.objects.filter(
        table=table, reserved_start_date__gte=reservation_start_date, reserved_start_date__lt=end_date)

    if (existingReservation.exists()):
        raise ValidationError("NOT ALLOWED!")

    reservation = Reservation.objects.create(
        guest=user, table=table, num_guests=num_guests, reserved_start_date=reservation_start_date)

    return reservation


def get_timeslots(num_guests, date):
    start_date = datetime(date.year, date.month, date.day, 0, 0)
    end_date = datetime(date.year, date.month, date.day, 23, 59)
    existingReservations = Reservation.objects.filter(table__capacity__gte=num_guests,
                                                      reserved_start_date__gte=start_date, reserved_start_date__lte=end_date)

    timeslots = []
    for hour in range(11, 22):
        timeslot = TimeSlot()
        timeslot.time = hour

        if any(x.reserved_start_date.hour == hour for x in existingReservations):
            timeslot.is_reserved = True
        else:
            timeslot.is_reserved = False

        timeslots.append(timeslot)

    return timeslots
