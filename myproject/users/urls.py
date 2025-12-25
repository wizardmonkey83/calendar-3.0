from django.urls import path
from .views import login_view, step_one_create, step_two_create, signup_view, load_step_one_signup, profile_view, load_profile_fragment, load_edit_profile, save_profile

urlpatterns = [
    # auth 
    path("signup/", signup_view, name="signup_view"),
    path("login/", login_view, name="login_view"),

    # profile
    path("profile/", profile_view, name="profile_view"),
    path("profile/edit/", load_edit_profile, name="load_edit_profile"),
    path("profile/edit/cancel/", load_profile_fragment, name="load_profile_fragment"),
    path("profile/save/", save_profile, name="save_profile"),

    # creating calendar
    path("create/step/1/", load_step_one_signup, name="load_step_one_signup"),
    path("create/step/2/", step_one_create, name="step_one_create"),
    path("create/step/3/", step_two_create, name="step_two_create"),
]