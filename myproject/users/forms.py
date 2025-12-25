from django import forms
from .models import CustomUser

# auth
class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())         
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10, required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput())
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())

# edit profile
class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput())
    last_name = forms.CharField(required=False, widget=forms.TextInput())
    phone_number = forms.CharField(max_length=10, required=False, widget=forms.TextInput())
    email = forms.EmailField(required=False, widget=forms.EmailInput())

# create calendar
class StepOneSignInForm(forms.Form):
    recipient_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g. The Avengers'}))
    # use emailinput instead of emailfield. dunno why.
    recipient_email_address = forms.CharField(max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'e.g. batman@gotham.com'}))

class StepTwoSignInForm(forms.Form):
    street_address = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    apt_suite = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    recipient_city = forms.CharField(max_length=100, required=False, widget=forms.TextInput())
    recipient_state = forms.CharField(max_length=50, required=False, widget=forms.TextInput())

class StepThreeSignInForm(forms.Form):
    recipient_bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea())   