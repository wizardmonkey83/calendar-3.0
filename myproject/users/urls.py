from django.urls import path
from .views import load_signup, load_login, step_one_signup, step_two_signup, signup_view

urlpatterns = [
    # signup 
    path("signup/step/1/", load_signup, name="load_signup"),
    path("signup/step/2/", step_one_signup, name="step_one_signup"),
    path("signup/step/3/", step_two_signup, name="step_two_signup"),
    path("signup/", signup_view, name="signup_view"),


    path("login/", load_login, name="load_login"),
]