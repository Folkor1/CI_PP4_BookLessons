from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('bookings/', views.BookingsView.as_view(), name="bookings"),
]