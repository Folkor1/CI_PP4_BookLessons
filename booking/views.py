from django.shortcuts import render


def homepage(request):
    """
    Render the home page
    """
    return render(request, "index.html")


class BookingsView(generic.ListView):
    """
    Render bookings page
    """
    template_name = "bookings.html"
