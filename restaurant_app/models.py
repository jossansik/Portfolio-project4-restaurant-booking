from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Booked"), (1, "Confirmed"))


class Table(models.Model):
    name = models.CharField(max_length=200, unique=True)
    capacity = models.IntegerField(db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Reservation(models.Model):
    num_guests = models.IntegerField(db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    reserved_start_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='guest_reservations')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='table_reservations')
