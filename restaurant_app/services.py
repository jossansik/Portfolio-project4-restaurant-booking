import pytz
from django.forms import ValidationError
from restaurant_app.models import MAX_HOUR, MIN_HOUR, Reservation, Table
from datetime import timedelta, datetime


class ReservedTable:
    def __init__(self):
        self.is_reserved = False,
        self.id = 0,


class ReservedTableTimeSlot:
    def __init__(self):
        self.time = 0,
        self.reservedTable = {},


class TimeSlot:
    def __init__(self):
        self.time = {},
        self.is_reserved = False,
        self.table_id = 0,


def make_reservation(user, table_id, reservation_start_date, num_guests, guest_fullname):
    table = Table.objects.get(pk=table_id)

    if any(Reservation.objects.filter(guest=user, reserved_start_date__gte=datetime.now(tz=pytz.UTC))):
        raise ValidationError(
            "You already have a reservation. Go to My reservation to view it.")

    if int(num_guests) > int(table.capacity):
        raise ValidationError(
            "Table does not support the requested guest count")

    end_date = reservation_start_date + timedelta(minutes=30)
    existingReservation = Reservation.objects.filter(
        table=table, reserved_start_date__gte=reservation_start_date, reserved_start_date__lt=end_date)

    if (existingReservation.exists()):
        raise ValidationError("Table is already reserved")

    reservation = Reservation.objects.create(
        guest=user, table=table, num_guests=num_guests, reserved_start_date=reservation_start_date, guest_fullname=guest_fullname)

    return reservation


def get_timeslots(num_guests, date):
    start_date = datetime(date.year, date.month, date.day, 0, tzinfo=pytz.UTC)
    end_date = datetime(date.year, date.month, date.day,
                        23, 59, tzinfo=pytz.UTC)
    tables = Table.objects.filter(capacity__gte=num_guests)
    reservedTableTimeslots = []
    for table in tables:
        existingReservations = Reservation.objects.filter(
            table=table, reserved_start_date__gte=start_date, reserved_start_date__lte=end_date)

        for hour in range(MIN_HOUR, MAX_HOUR):
            reservedTableTimeslot = ReservedTableTimeSlot()
            reservedTableTimeslot.time = hour
            reservedTableTimeslot.reservedTable = ReservedTable()
            reservedTableTimeslot.reservedTable.id = table.id

            if any(x.reserved_start_date.hour == hour for x in existingReservations):
                reservedTableTimeslot.reservedTable.is_reserved = True
            else:
                reservedTableTimeslot.reservedTable.is_reserved = False

            reservedTableTimeslots.append(reservedTableTimeslot)

    timeslots = []
    for hour in range(MIN_HOUR, MAX_HOUR):
        timeslot = TimeSlot()
        timeslot.time = datetime(
            date.year, date.month, date.day, hour, tzinfo=pytz.UTC)
        timeslot.num_guests = num_guests

        reservedTableTimeslotsForHour = (
            x for x in reservedTableTimeslots if x.time == hour)
        is_reserved = all(v.reservedTable.is_reserved ==
                          True for v in reservedTableTimeslotsForHour)

        if is_reserved:
            timeslot.is_reserved = True
        else:
            randomTablesInAvailableHour = (
                x for x in reservedTableTimeslots if x.time == hour)
            timeslot.table_id = int(
                list(randomTablesInAvailableHour)[0].reservedTable.id)
            timeslot.is_reserved = False

        timeslots.append(timeslot)

    return timeslots
