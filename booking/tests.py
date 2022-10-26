from django.test import TestCase
import unittest2
from .models import Bookings
from django.contrib.auth.models import User
from datetime import date, time


class TestDates(unittest2.TestCase):
    """
    Check Bookings.expired() function
    """

    def setUp(self):
        Bookings.objects.create(
            lesson='Theory',
            lesson_type='Offline',
            date='2030-10-24',
            time='12:00',
            student_id=1,
            status=True
            )
        Bookings.objects.create(
            lesson='Piano',
            lesson_type='Offline',
            date='2022-10-24',
            time='12:00',
            student_id=1,
            status=True
            )
        Bookings.expired()
