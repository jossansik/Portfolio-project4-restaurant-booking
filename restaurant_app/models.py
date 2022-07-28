from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Booked"), (1, "Confirmed"))
TYPE = ((0, "Dishes"), (1, "Drinks"))
MAX_TABLE_CAPACITY = 8
MIN_TABLE_CAPACITY = 2
MIN_HOUR = 11
MAX_HOUR = 22


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
    guest_fullname = models.CharField(max_length=150)


class Menu(models.Model):
    type = models.IntegerField(choices=TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True)
    image = CloudinaryField('image', default='media/default.jpg')
    position = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=300, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')
    position = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
