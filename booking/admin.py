from django.contrib import admin
from .models import Bookings


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    """
    Class for bookings admin model
    """
    list_display = ('lesson', 'lesson_type', 'time', 'date', 'status', 'student')
    search_fields = ['lesson', 'lesson_type', 'date', 'status', 'student']
    list_filter = ('lesson', 'lesson_type', 'date', 'status', 'student')
