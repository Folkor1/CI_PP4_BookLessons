from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from .models import Bookings
from django.http import HttpResponseRedirect
from django.contrib import messages


def homepage(request):
    """
    Render the home page
    """
    return render(request, "index.html")


class BookingsView(generic.ListView):
    """
    Render bookings page
    """
    model = Bookings
    template_name = "bookings.html"

    def post(self, request):
        """
        Create new booking
        """
        if request.method == 'POST':
            lesson = request.POST.get('lesson_inp')
            lesson_type = request.POST.get('lesson_type_inp')
            date = request.POST.get('date_inp')
            time = request.POST.get('time_inp')
            status = True
            student = request.user
            booking = Bookings(lesson=lesson, lesson_type=lesson_type, date=date, time=time, status=status, student=student)
            booking.save()
            messages.success(request, 'Booking successfully added.')
            return HttpResponseRedirect(reverse('manage_bookings'))


class ManageBookingsView(generic.ListView):
    """
    Render manage bookings page
    """
    model = Bookings
    template_name = "manage_bookings.html"
