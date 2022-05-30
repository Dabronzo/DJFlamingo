from django import forms
from .models import Gig, Venue
from django.forms import ModelForm


class DateInput(forms.DateInput):
    """Class to overwrite the DateTimeInput of Django"""
    input_type = 'date'


class GigCreationForm(ModelForm):
    """Class form to gigs"""

    date = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control', 'placeholder': ''})
        )
    is_payed = forms.BooleanField(required=False)

    class Meta:
        """Meta class for widgets"""
        model = Gig
        fields = (
            'name',
            'date',
            'time_start',
            'time_duration',
            'dj',
            'venue',
            'fees',
            'agency_tax',
            'is_payed',
            'status',
            'notes'
            )

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Event Name'}
                ),
            'time_start': forms.TimeInput(
                attrs={'type': 'time'}
                ),
            'time_duration': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'eg: 1 hour'}
                ),
            'dj': forms.Select(
                attrs={
                    'class': 'form-select form-control',
                    'placeholder': 'DJ'
                    }
                ),
            'venue': forms.Select(
                attrs={
                    'class': 'form-select form-control',
                    'placeholder': 'Select a venue'
                    }
                ),
            'fees': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '0.00'}
                ),
            'agency_tax': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-select form-control',
                    'placeholder': 'Select the status of the gig'
                    }
                ),
            'notes': forms.Textarea(
                attrs={'class': 'form-control'}
                ),
        }


class VenueCreationForm(ModelForm):
    """Class form to venue"""

    class Meta:
        """Meta for widgets"""

        model = Venue
        fields = (
            'name',
            'address',
            'city',
            'website',
            'contact',
            'additional_info'
            )

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Venue Name'}
                ),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Address'}
                ),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'City'}
                ),
            'contact': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Contact Info'}
                ),
            'website': forms.URLInput(
                attrs={'class': 'form-control'}
                ),
            'additional_info': forms.Textarea(
                attrs={'class': 'form-control'}
                ),
        }
