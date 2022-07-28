import pytz
from django.forms import ValidationError
from restaurant_app.models import MAX_HOUR, MIN_HOUR, Menu, MenuItem, Reservation, Table
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


class MenuViewModel:
    def __init__(self):
        self.name = '',
        self.description = '',
        self.image = '',
        self.items = []


class MenuViewModelItem:
    def __init__(self):
        self.name = '',
        self.description = '',
        self.price = 0,


def make_reservation(user, table_id, start_date, num_guests, guest_fullname):
    start_date = datetime(year=start_date.year, month=start_date.month, day=start_date.day,
                          hour=start_date.hour, minute=0, tzinfo=pytz.UTC)
    table = Table.objects.get(pk=table_id)

    current_date = datetime.now(tz=pytz.UTC)
    unbookable_date_from = datetime(year=current_date.year, month=current_date.month,
                                    day=current_date.day, hour=current_date.hour, minute=0, tzinfo=pytz.UTC)
    if any(Reservation.objects.filter(guest=user, reserved_start_date__gte=unbookable_date_from)):
        raise ValidationError(
            "You already have a reservation. Go to My reservation to view it.")

    if int(num_guests) > int(table.capacity):
        raise ValidationError(
            "Table does not support the requested guest count")

    end_date = start_date + timedelta(hours=1)

    existing_reservation = Reservation.objects.filter(
        table=table, reserved_start_date__gte=start_date, reserved_start_date__lt=end_date)

    if (existing_reservation.exists()):
        raise ValidationError("Table is already reserved")

    reservation = Reservation.objects.create(
        guest=user, table=table, num_guests=num_guests, reserved_start_date=start_date, guest_fullname=guest_fullname)

    return reservation


def get_timeslots(num_guests, date):
    start_date = datetime(date.year, date.month, date.day, 0, tzinfo=pytz.UTC)
    end_date = datetime(date.year, date.month, date.day,
                        23, 59, tzinfo=pytz.UTC)
    tables = Table.objects.filter(capacity__gte=num_guests)
    reserved_table_timeslots = []
    for table in tables:
        existing_reservations = Reservation.objects.filter(
            table=table, reserved_start_date__gte=start_date, reserved_start_date__lte=end_date)

        for hour in range(MIN_HOUR, MAX_HOUR):
            reserved_table_timeslot = ReservedTableTimeSlot()
            reserved_table_timeslot.time = hour
            reserved_table_timeslot.reservedTable = ReservedTable()
            reserved_table_timeslot.reservedTable.id = table.id

            if any(x.reserved_start_date.hour == hour for x in existing_reservations):
                reserved_table_timeslot.reservedTable.is_reserved = True
            else:
                reserved_table_timeslot.reservedTable.is_reserved = False

            reserved_table_timeslots.append(reserved_table_timeslot)

    timeslots = []
    for hour in range(MIN_HOUR, MAX_HOUR):
        timeslot = TimeSlot()
        timeslot.time = datetime(
            date.year, date.month, date.day, hour, tzinfo=pytz.UTC)
        timeslot.num_guests = num_guests

        reserved_table_timeslots_for_hour = (
            x for x in reserved_table_timeslots if x.time == hour)
        is_reserved = all(v.reservedTable.is_reserved ==
                          True for v in reserved_table_timeslots_for_hour)

        if is_reserved:
            timeslot.is_reserved = True
        else:
            random_tables_in_available_hour = (
                x for x in reserved_table_timeslots if x.time == hour)
            timeslot.table_id = int(
                list(random_tables_in_available_hour)[0].reservedTable.id)
            timeslot.is_reserved = False

        timeslots.append(timeslot)

    return timeslots


def get_menus(type):
    menus = []

    model_menus = Menu.objects.filter(type=type).order_by('position')

    for model_menu in model_menus:
        menu = MenuViewModel()
        menu.name = model_menu.name
        menu.description = model_menu.description
        menu.image = model_menu.image
        model_menu_items = MenuItem.objects.filter(
            menu=model_menu).order_by('position')

        for model_menu_item in model_menu_items:
            menu_item = MenuViewModelItem()
            menu_item.name = model_menu_item.name
            menu_item.description = model_menu_item.description
            menu_item.price = model_menu_item.price

            menu.items.append(menu_item)

        menus.append(menu)

    return menus
