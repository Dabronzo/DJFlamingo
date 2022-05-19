from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewDjUser


class RegistrationForm(UserCreationForm):
    """Class form for register new user/dj"""

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}
        ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': ''}
        ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': ''}
        ))

    class Meta:
        """Widgets and format"""

        model = NewDjUser
        fields = ('email', 'user_name', 'password1', 'password2')

        widgets = {
            'user_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'DJ Name'}
                ),
        }
