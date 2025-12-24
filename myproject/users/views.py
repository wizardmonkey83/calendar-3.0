from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import SignUpForm, LoginForm, StepOneSignInForm, StepTwoSignInForm, StepThreeSignInForm

User = get_user_model()

# Create your views here.
def load_signup(request):
    form = SignUpForm
    return render(request, "users/signup/signup.html", {"form": form})

def load_login(request):
    form = LoginForm
    return render(request, "users/login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
                form.add_error(None, "Email or Phone Number already in use")
                return render(request, "users/signup/signup.html", {"form": form})
            if password1 != password2:
                form.add_error(None, "Passwords don't match")
                return render(request, "users/signup/signup.html", {"form": form})
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password1)
            login(request, user)
            return redirect("load_home")
    else:
        form = SignUpForm
        return render(request, "users/signup/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                
                return redirect("problem_list_window")
            else:
                form.add_error(None, "Invalid Email or Password")
            
    else:
        form = LoginForm()
    
    return render(request, "accounts/login.html", {"form": form})

@login_required
def load_step_one_signup(request):
    form = StepOneSignInForm
    return render(request, "user/signup/step_1.html", {"form": form})

@login_required
def step_one_create(request):
    if request.method == "POST":
        form = StepOneSignInForm(request.POST)
        if form.is_valid():
            recipient_name = form.cleaned_data["recipient_name"]
            recipient_email_address = form.cleaned_data["recipient_email_address"]

            if User.objects.filter(email=recipient_email_address).exists():
                form.add_error(None, "Email or Username already exists")
                return render(request, "users/signup/step_1.html", {"form": form})


            # think this is going to be easiest
            request.session["arytes_help_recipient_name"] = recipient_name
            request.session["arytes_help_recipient_email_address"] = recipient_email_address
            
            return render(request, "users/signup/step_2.html", {"form": StepTwoSignInForm})

@login_required
def step_two_create(request):
    if request.method == "POST":
        form = StepTwoSignInForm(request.POST)
        # this might fail if fields arent entered even if they arent "required"
        if form.is_valid():
            street_address = form.cleaned_data["street_address"]
            recipient_city = form.cleaned_data["recipient_city"]
            recipient_state = form.cleaned_data["recipient_state"]
            apt_suite = form.cleaned_data["apt_suite"]

            if street_address:
                request.session["arytes_help_street_address"] = street_address
            if apt_suite:
                request.session["arytes_help_apt_suite"] = apt_suite
            if recipient_state:
                request.session["arytes_help_recipient_state"] = recipient_state
            if recipient_city:
                request.session["arytes_help_recipient_city"] = recipient_city

            return render(request, "users/signup/step_3.html", {"form": StepThreeSignInForm})

@login_required     
def step_three_create(request):
    return None

