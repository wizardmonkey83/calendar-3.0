from django.urls import path
from .views import load_signup, load_login, step_one_signup

urlpatterns = [
    # signup 
    path("signup/", load_signup, name="load_signup"),
    path("signup/step/2/", step_one_signup, name="step_one_signup"),


    path("login/", load_login, name="load_login"),
]