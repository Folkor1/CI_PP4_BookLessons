from django.shortcuts import render
from booking.models import Bookings
from django.core.exceptions import PermissionDenied
from booking.filters import BookingFilter


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
