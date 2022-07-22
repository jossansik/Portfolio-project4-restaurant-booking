from django.contrib import admin
from .models import Reservation, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
    list_filter = ('created_on',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest', 'table', 'reserved_start_date',
                    'num_guests', 'status')
    list_filter = ('status', 'created_on')
