from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Gig


class GigFilter(FilterSet):
    """Filter class to the admin gigs table"""

    date = DateFilter(
        field_name='date',
        lookup_expr='gte',
        label='Start Date',
        input_formats=["%d/%m/%Y"],
        widget=DateInput(attrs={'placeholder': 'dd/mm/yy'}),
        )

    end_date = DateFilter(
        field_name='date',
        lookup_expr='lte',
        label='End Date',
        input_formats=["%d/%m/%Y"],
        widget=DateInput(attrs={'placeholder': 'dd/mm/yy'}),
    )

    class Meta:

        model = Gig
        fields = ('venue', 'dj', 'date')
