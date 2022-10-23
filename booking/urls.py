from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('bookings/', views.BookingsView.as_view(), name="bookings"),
    path('manage_bookings/', views.ManageBookingsView.as_view(), name='manage_bookings'),
    path('edit/<booking_id>', views.edit_booking_date, name="edit"),
    path('edit_type/<booking_id>', views.edit_booking_type, name="edit_type"),
    path('cancel/<booking_id>', views.cancel_booking, name="cancel"),
    path('past_bookings/', views.PastBookingsView.as_view(), name="past_bookings"),
    path('admin_panel/', views.admin_panel, name="admin_panel"),
    path('admin_past_bookings/', views.admin_past_bookings, name="admin_past_bookings"),
    path('admin_upcoming_bookings/', views.admin_upcoming_bookings, name="admin_upcoming_bookings")
]