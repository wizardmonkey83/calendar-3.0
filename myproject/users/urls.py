from django.urls import path
from .views import login_view, step_one_create, step_two_create, signup_view, load_step_one_signup

urlpatterns = [
    # auth 
    path("signup/", signup_view, name="signup_view"),
    path("login/", login_view, name="login_view"),

    path("create/step/1/", load_step_one_signup, name="load_step_one_signup"),
    path("create/step/2/", step_one_create, name="step_one_create"),
    path("create/step/3/", step_two_create, name="step_two_create"),
]