from django.shortcuts import render
from django.views import generic


class AboutView(generic.ListView):
    """
    Render about page
    """
    model = About
    template_name = "about.html"
