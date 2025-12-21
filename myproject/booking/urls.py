from django.urls import path

from .views import load_home

urlpatterns = [
    path("home/", load_home, name="load_home"),
]