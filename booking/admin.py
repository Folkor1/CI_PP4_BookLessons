from django.contrib import admin
from .models import Bookings, About
from django import template


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    """
    Class for bookings admin model
    """
    list_display = (
        'lesson',
        'lesson_type',
        'time', 'date',
        'status',
        'student')
    search_fields = ['lesson', 'lesson_type', 'date', 'status', 'student']
    list_filter = ('lesson', 'lesson_type', 'date', 'status', 'student')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Class for About Admin model
    """
    list_display = ('title', 'text', 'image')
