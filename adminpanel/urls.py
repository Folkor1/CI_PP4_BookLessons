from django.urls import path
from . import views


urlpatterns = [

    path('admin_panel/', views.admin_panel, name="admin_panel"),
]
