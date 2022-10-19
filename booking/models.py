from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


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
