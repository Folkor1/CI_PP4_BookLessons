"""bookingpiano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls'), name='booking_urls'),
    path('accounts/', include('allauth.urls')),
    path('', include(
        ('adminpanel.urls', 'admin_panel'),
        namespace='adminpanel')
        ),
    path('', include(
        ('adminpanel.urls', 'admin_past_bookings'),
        namespace='admin_past_bookings')
        ),
    path('', include(
        ('adminpanel.urls', 'admin_upcoming_bookings'),
        namespace='admin_upcoming_bookings')
        ),
    path('', include(
        ('home.urls', 'homepage'),
        namespace='homepage')
        ),
    path('', include(
        ('booking.urls', 'bookings'),
        namespace='bookings')
        ),
    path('', include(
        ('booking.urls', 'cancel_booking'),
        namespace='cancel_booking')
        ),
    path('', include(
        ('booking.urls', 'edit_booking_date'),
        namespace='edit_booking_date')
        ),
    path('', include(
        ('booking.urls', 'edit_booking_type'),
        namespace='edit_booking_type')
        ),
    path('', include(
        ('booking.urls', 'manage_bookings'),
        namespace='manage_bookings')
        ),
    path('', include(
        ('booking.urls', 'past_bookings'),
        namespace='past_bookings')
        ),
    path('', include(
        ('about.urls', 'about'),
        namespace='about')
        ),
]
