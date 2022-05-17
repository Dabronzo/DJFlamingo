from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Gig
from .forms import GigCreationForm, VenueCreationForm
from django.core.paginator import Paginator


class LandingGigsView(View):
    """View class to handle the gigs list or the landing page"""

    def get(self, request, *args, **kwargs):
        
        logged_in = self.request.user
        if logged_in.id is None:
            return render(
                request, 'landing.html'
                )
        elif logged_in.is_superuser:
            queryset = Gig.objects.order_by('date')
           
            return render(
                request, 'staff.html',
                {
                    'all_gigs': queryset,
                }
            )
        else:
            queryset = Gig.objects.filter(dj=logged_in).order_by('date')
            gigs_exclude_reject = queryset.exclude(status=2).order_by('date')

            lsit_gigs = []
            for gig in gigs_exclude_reject:
                if gig.days_to >= 0:
                    lsit_gigs.append(gig)

            # Pagination
            p = Paginator(lsit_gigs, 8)
            page = request.GET.get('page')
            my_gigs = p.get_page(page)

            return render(
                request, 'index.html',
                {
                    'my_gigs': my_gigs,
                }
            )


class CreateGig(View):
    """View Class to show the fomr to create a new gig"""

    def get(self, request, *args, **kwargs):

        form = GigCreationForm()
        return render(
            request, 'create_gig.html',
            {
                'form': form,
            }
        )
    
    def post(self, request, *args, **kwargs):
        """Post Method to create gig"""

        form = GigCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')


class CreateVenue(View):
    """View class for the venue creation"""

    def get(self, request, *args, **kwargs):
        """Get to show the form and template"""

        form = VenueCreationForm()
        return render(
            request, 'create_venue.html',
            {
                'form': form,
            }
        )
    
    def post(self, request, *args, **kwargs):
        """Post to create a venue"""

        form = VenueCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')


