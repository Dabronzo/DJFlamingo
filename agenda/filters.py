from django_filters import FilterSet
from .models import Gig


class GigFilter(FilterSet):
    """Filter class to the admin gigs table"""

    class Meta:

        model = Gig
        fields = ('date', 'venue', 'dj')
