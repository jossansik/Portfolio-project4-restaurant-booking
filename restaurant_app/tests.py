import unittest
from django.forms import ValidationError
from django.test import TestCase
from datetime import datetime
from restaurant_app.models import Table, Reservation
from restaurant_app.services import makereservation
from django.contrib.auth.models import User


class TableTest(TestCase):

    def create_table(self, capacity=3):
        return Table.objects.create(capacity=capacity)

    def test_can_create_table(self):
        w = self.create_table()
        self.assertTrue(isinstance(w, Table))
        self.assertEqual(3, w.capacity)


class ReservationTest(TestCase):

    def create_reservation(self, tableCapacity=3, username="Kons", num_guests=3, reserved_start_date=datetime.now()):
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
        reserved_start_date = datetime.now()
        capacity = 4
        number_of_guests = 3
        table = Table.objects.create(capacity=capacity)
        userWithReservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')

        # Act
        reservation = makereservation(
            userWithReservation, table, reserved_start_date, number_of_guests)

        # Assert
        self.assertEqual(reservation.reserved_start_date, reserved_start_date)
        self.assertEqual(reservation.num_guests, number_of_guests)
        self.assertEqual(reservation.table.capacity, capacity)

    def test_guest_cannot_reserve_booked_table_at_fully_booked_time(self):
        # Arrange
        reserved_start_date = datetime.now()
        capacity = 4
        number_of_guests = 3
        table = Table.objects.create(capacity=capacity)
        userWithReservation = User.objects.create_user(
            "Sven", 'sven@ripa.com', 'testpassword')
        Reservation.objects.create(guest=userWithReservation, table=table,
                                   num_guests=number_of_guests, reserved_start_date=reserved_start_date)
        userWantToReservate = User.objects.create_user(
            "Janne", 'janne@svensson.com', 'testpassword')

        # Act & Assert
        with self.assertRaises(ValidationError) as context:
            makereservation(userWantToReservate, table.id,
                            reserved_start_date, number_of_guests)
        self.assertTrue('NOT ALLOWED!' in str(context.exception))
