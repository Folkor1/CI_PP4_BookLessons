import django_filters
from .models import Bookings


class BookingFilter(django_filters.FilterSet):
    """
    Class student filter
    """

    class Meta:
        model = Bookings
        fields = {'student': ['exact']}
