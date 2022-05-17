from django_filters import FilterSet
from .models import Gig


class GigFilter(FilterSet):
    """Filter class to the admin gigs table"""
    model = Gig
    fields = '__all__'

