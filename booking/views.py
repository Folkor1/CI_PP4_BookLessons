from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from .models import Bookings, About
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .filters import BookingFilter


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

    def get(self, request, *args, **kwargs):
        """
        Hide past dates
        """
        Bookings.expired()
        return super().get(request, *args, **kwargs)

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
            booking = Bookings(
                lesson=lesson,
                lesson_type=lesson_type,
                date=date,
                time=time,
                status=status,
                student=student)
            booking.save()
            messages.success(request, 'Booking successfully added.')
            return HttpResponseRedirect(reverse('manage_bookings'))


class ManageBookingsView(generic.ListView):
    """
    Render manage bookings page
    """
    model = Bookings
    template_name = "manage_bookings.html"

    def get(self, request, *args, **kwargs):
        """
        Hide past dates
        """
        Bookings.expired()
        return super().get(request, *args, **kwargs)


def edit_booking_date(request, booking_id):
    """
    Edit booking date and time
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.date = request.POST.get('edit_date_inp')
        booking.time = request.POST.get('edit_time_inp')
        booking.save()
        messages.success(request, 'Date successfully changed.')
        return redirect('manage_bookings')
    context = {
        'edit_date_lesson': Bookings.get_lesson(booking),
        'edit_date_lesson_type': Bookings.get_lesson_type(booking)
        }
    return render(request, 'edit_booking_date.html', context)


def edit_booking_type(request, booking_id):
    """
    Edit lesson type
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.lesson_type = request.POST.get('edit_lesson_type')
        booking.save()
        messages.success(request, 'Lesson type successfully changed.')
        return redirect('manage_bookings')
    context = {
        'edit_date_lesson_type': Bookings.get_lesson_type(booking)
        }
    return render(request, 'edit_booking_type.html', context)


def cancel_booking(request, booking_id):
    """
    Cancel booking
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Lesson successfully canceled.')
        return redirect('manage_bookings')
    context = {
        'cancel_lesson': Bookings.get_lesson(booking),
        'cancel_lesson_type': Bookings.get_lesson_type(booking),
        'cancel_date': Bookings.get_date(booking),
        'cancel_time': Bookings.get_time(booking)
        }
    return render(request, 'cancel_booking.html', context)


class PastBookingsView(generic.ListView):
    """
    Render past bookings page
    """
    model = Bookings
    paginate_by = 19
    template_name = "past_bookings.html"


def admin_panel(request):
    """
    Render admin panel
    """
    admin_piano = Bookings.objects.filter(lesson='Piano').count()
    admin_theory = Bookings.objects.filter(lesson='Theory').count()
    admin_online = Bookings.objects.filter(lesson_type='Online').count()
    admin_offline = Bookings.objects.filter(lesson_type='Offline').count()
    admin_completed = Bookings.objects.filter(status='False').count()
    admin_upcoming = Bookings.objects.filter(status='True').count()
    admin_total = Bookings.objects.all().count()
    context = {
        'admin_piano': admin_piano,
        'admin_theory': admin_theory,
        'admin_online': admin_online,
        'admin_offline': admin_offline,
        'admin_total': admin_total,
        'admin_completed': admin_completed,
        'admin_upcoming': admin_upcoming,
    }
    if not request.user.is_superuser:
        raise PermissionDenied

    return render(request, "admin_panel.html", context)


def admin_past_bookings(request):
    """
    Render admin past bookings
    """
    booking = Bookings.objects.filter(status=False)
    booking_filter = BookingFilter(request.GET, queryset=booking)
    context = {
        'booking_filter': booking_filter
    }
    if not request.user.is_superuser:
        raise PermissionDenied
    return render(request, "admin_past_bookings.html", context)


def admin_upcoming_bookings(request):
    """
    Render admin upcoming bookings
    """
    future_lessons = Bookings.objects.filter(status=True)
    future_filter = BookingFilter(request.GET, queryset=future_lessons)
    context = {
        'future_filter': future_filter
    }
    if not request.user.is_superuser:
        raise PermissionDenied
    return render(request, "admin_upcoming_bookings.html", context)


class AboutView(generic.ListView):
    """
    Render about page
    """
    model = About
    template_name = "about.html"
