from django.urls import path
from . import views


urlpatterns = [

    path('admin_panel/', views.admin_panel, name="admin_panel"),
    path(
        'admin_past_bookings/',
        views.admin_past_bookings,
        name="admin_past_bookings"
        ),
]
