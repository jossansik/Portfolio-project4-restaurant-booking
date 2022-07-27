import pytz
from django.forms import ValidationError
from django.test import TestCase
from datetime import datetime, timedelta
from restaurant_app.models import MIN_HOUR, Table, Reservation
from restaurant_app.services import make_reservation, get_timeslots
from django.contrib.auth.models import User


class TableTest(TestCase):

    def create_table(self, capacity=3):
        return Table.objects.create(capacity=capacity)

    def test_can_create_table(self):
        w = self.create_table()
        self.assertTrue(isinstance(w, Table))
        self.assertEqual(3, w.capacity)


class ReservationTest(TestCase):

    def create_reservation(self, tableCapacity=3, username="Kons", num_guests=3, reserved_start_date=datetime.now(tz=pytz.UTC)):
        table = Table.objects.create(capacity=tableCapacity)
        user = User.objects.create_user(
            username, 'blah@blah.com', 'testpassword')
        reservation = Reservation.objects.create(
            guest=user, table=table, num_guests=num_guests, reserved_start_date=reserved_start_date)
        return reservation

    def test_guest_can_reservate_table(self):
        w = self.create_reservation()
        self.assertTrue(isinstance(w, Reservation))
        self.assertEqual(3, w.table.capacity)
        self.assertEqual("Kons", w.guest.username)


class ReserveTableTest(TestCase):

    def test_guest_can_reserve_available_table(self):
        # Arrange
        reserved_start_date = datetime.now(tz=pytz.UTC)
        capacity = 4
        number_of_guests = 3
        table = Table.objects.create(capacity=capacity)
        user_with_reservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        guest_fullname = 'Jan Svensson'

        # Act
        reservation = make_reservation(
            user_with_reservation, table.id, reserved_start_date, number_of_guests, guest_fullname)

        # Assert
        self.assertEqual(reservation.reserved_start_date, reserved_start_date)
        self.assertEqual(reservation.num_guests, number_of_guests)
        self.assertEqual(reservation.table.capacity, capacity)

    def test_guest_cannot_reserve_booked_table_at_fully_booked_time(self):
        # Arrange
        reserved_start_date = datetime.now(tz=pytz.UTC)
        capacity = 4
        number_of_guests = 3
        table = Table.objects.create(capacity=capacity)
        user_with_reservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        guest_fullname = 'Karl Swedensson'
        Reservation.objects.create(guest=user_with_reservation, table=table,
                                   num_guests=number_of_guests, reserved_start_date=reserved_start_date, guest_fullname=guest_fullname)
        user_want_to_reservate = User.objects.create_user(
            "Janne", 'janne@svensson.com', 'testpassword')
        user_want_to_reservate_guest_fullname = 'Super Duper'

        # Act & Assert
        with self.assertRaises(ValidationError) as context:
            make_reservation(user_want_to_reservate, table.id,
                             reserved_start_date, number_of_guests, user_want_to_reservate_guest_fullname)
        self.assertTrue('Table is already reserved' in str(context.exception))

    def test_guest_cannot_reserve_table_without_capacity(self):
        # Arrange
        reserved_start_date = datetime.now(tz=pytz.UTC)
        capacity = 4
        number_of_guests = 5
        table = Table.objects.create(name="Table 1", capacity=capacity)
        user = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        guest_fullname = 'Jonas Petersson'

        # Act & Assert
        with self.assertRaises(ValidationError) as context:
            make_reservation(user, table.id, reserved_start_date,
                             number_of_guests, guest_fullname)
        self.assertTrue(
            'Table does not support the requested guest count' in str(context.exception))

    def test_guest_cannot_have_multiple_active_reservations(self):
        # Arrange
        reserved_start_date = datetime.now(tz=pytz.UTC) + timedelta(hours=1)
        prev_booking_date = reserved_start_date
        capacity = 4
        number_of_guests = 2
        table = Table.objects.create(name="Table 1", capacity=capacity)
        user = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        guest_fullname = 'Jonas Petersson'
        make_reservation(user, table.id, prev_booking_date,
                         number_of_guests, guest_fullname)

        # Act & Assert
        with self.assertRaises(ValidationError) as context:
            make_reservation(
                user, table.id, reserved_start_date, number_of_guests, guest_fullname)
        self.assertTrue('You already have a reservation. Go to My reservation to view it.' in str(
            context.exception))

    def test_guest_can_have_a_previous_reservation_and_make_a_new(self):
        # Arrange
        reserved_start_date = datetime.now(tz=pytz.UTC)
        prev_booking_date = reserved_start_date - timedelta(days=1)
        capacity = 4
        number_of_guests = 2
        table = Table.objects.create(name="Table 1", capacity=capacity)
        user = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        guest_fullname = 'Jonas Petersson'
        make_reservation(user, table.id, prev_booking_date,
                         number_of_guests, guest_fullname)

        # Act
        reservation = make_reservation(
            user, table.id, reserved_start_date, number_of_guests, guest_fullname)

        # Assert
        self.assertEqual(reservation.reserved_start_date, reserved_start_date)
        self.assertEqual(reservation.num_guests, number_of_guests)
        self.assertEqual(reservation.table.capacity, capacity)


class ReservationTimesTest(TestCase):

    def test_guest_can_list_reservations(self):
        # Arrange
        date = datetime.now(tz=pytz.UTC)
        start_date = datetime(date.year, date.month,
                              date.day, MIN_HOUR, tzinfo=pytz.UTC)
        capacity = 4
        number_of_guests = 3
        guest_fullname = 'Karl Swedensson'
        table = Table.objects.create(name="Table 1", capacity=capacity)
        Table.objects.create(name="Table 2", capacity=capacity)
        user_with_reservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        make_reservation(user_with_reservation, table.id,
                         start_date, number_of_guests, guest_fullname)

        # Act
        timeslots = get_timeslots(num_guests=number_of_guests, date=date)

        # Assert
        self.assertEqual(timeslots[0].is_reserved, False)
        self.assertEqual(timeslots[1].is_reserved, False)

    # When there are multiple tables with requested capacities,
    # Only one table is reserved by a guest,
    # Guest should be able to reserve available table.
    def test_guest_can_view_available_table_for_timeslots(self):
        # Arrange
        date = datetime.now(tz=pytz.UTC)
        start_date = datetime(date.year, date.month,
                              date.day, MIN_HOUR, tzinfo=pytz.UTC)
        capacity = 4
        number_of_guests = 3
        guest_fullname = 'Karl Swedensson'
        table = Table.objects.create(name="Table 1", capacity=capacity)
        Table.objects.create(name="Table 2", capacity=capacity)
        user_with_reservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        make_reservation(user_with_reservation, table.id,
                         start_date, number_of_guests, guest_fullname)

        # Act
        timeslots = get_timeslots(num_guests=number_of_guests, date=date)

        # Assert
        self.assertEqual(timeslots[0].is_reserved, False)
        self.assertEqual(timeslots[1].is_reserved, False)

    def test_guest_can_view_reserved_timeslots(self):
        # Arrange
        date = datetime.now(tz=pytz.UTC)
        start_date = datetime(date.year, date.month,
                              date.day, MIN_HOUR, tzinfo=pytz.UTC)
        capacity = 4
        number_of_guests = 3
        guest_fullname = 'Karl Swedensson'
        table = Table.objects.create(capacity=capacity)
        userWithReservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        make_reservation(userWithReservation, table.id,
                         start_date, number_of_guests, guest_fullname)

        # Act
        timeslots = get_timeslots(num_guests=number_of_guests, date=date)

        # Assert
        self.assertEqual(timeslots[0].is_reserved, True)
        self.assertEqual(timeslots[0].time, datetime(
            date.year, date.month, date.day, MIN_HOUR, tzinfo=pytz.UTC))

        availableHour = MIN_HOUR+1
        self.assertEqual(timeslots[1].is_reserved, False)
        self.assertEqual(timeslots[1].table_id, table.id)
        self.assertEqual(timeslots[1].num_guests, number_of_guests)
        self.assertEqual(timeslots[1].time, datetime(
            date.year, date.month, date.day, availableHour, tzinfo=pytz.UTC))
