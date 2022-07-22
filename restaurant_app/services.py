from django.forms import ValidationError
from restaurant_app.models import Reservation
from datetime import timedelta


def makereservation(user, table, reservation_start_date, num_guests):
    end_date = reservation_start_date + timedelta(hours=1)
    existingReservation = Reservation.objects.filter(
        table=table, reserved_start_date__gte=reservation_start_date, reserved_start_date__lt=end_date)

    if (existingReservation.exists()):
        raise ValidationError("NOT ALLOWED!")

    reservation = Reservation.objects.create(
        guest=user, table=table, num_guests=num_guests, reserved_start_date=reservation_start_date)

    return reservation
