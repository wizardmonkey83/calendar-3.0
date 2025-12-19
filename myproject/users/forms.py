from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
            
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"placeholder": "Phone Number"}))
    home_address = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Home Address (Optional)"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Email"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name",)
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            # "password1": forms.PasswordInput(attrs={"placeholder": "Password"}),
            # "password2": forms.PasswordInput(attrs={"placeholder": "Re-enter Password"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
        }

        # gets rid of the helptext that automatically appears 
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # this is an attempt to make these fields required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
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


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))