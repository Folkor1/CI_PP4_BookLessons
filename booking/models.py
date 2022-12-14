from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Bookings(models.Model):
    """
    Class for Bookings model
    """
    lesson = models.CharField(max_length=50)
    lesson_type = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_lesson(self):
        """
        Return lesson name
        """
        return self.lesson

    def get_lesson_type(self):
        """
        Return lesson type name
        """
        return self.lesson_type

    def get_date(self):
        """
        Return date
        """
        return self.date

    def get_time(self):
        """
        Return time
        """
        return self.time

    def get_student(self):
        """
        Return student
        """
        return self.student

    def expired():
        """
        Set past dates to false
        """
        now = date.today()
        book = Bookings.objects.all()
        for b in book:
            if now > b.date:
                b.status = False
                b.save()

    class Meta:
        ordering = ['-date']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
