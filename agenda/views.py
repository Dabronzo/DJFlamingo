from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Gig
from .forms import GigCreationForm, VenueCreationForm
from django.core.paginator import Paginator
from .filters import GigFilter


class LandingGigsView(View):
    """View class to handle the gigs list or the landing page"""

    def get(self, request, *args, **kwargs):
        
        logged_in = self.request.user
        if logged_in.id is None:
            return render(
                request, 'landing.html'
                )
        elif logged_in.is_superuser:
            queryset = Gig.objects.all().order_by('date')

            my_filter = GigFilter(self.request.GET, queryset=queryset)
            all_gigs = my_filter.qs
             
            return render(
                request, 'staff.html',
                {
                    'all_gigs': all_gigs,
                    'my_filter': my_filter,
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


class DeleteGig(View):
    """Delete a gig from the database"""

    def post(self, request, slug, *args, **kwargs):
        """Post to delete"""

        gig = get_object_or_404(Gig, slug=slug)
        gig.delete()

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


class GigDetails(View):
    """Class view to the details of a specific gig"""

    def get(self, request, slug, *args, **kwargs):
        """ Method to render the Gig Details"""
        queryset = Gig.objects.all()
        gig = get_object_or_404(queryset, slug=slug)
        venue = gig.venue

        return render(
            request, 'gig_details.html',
            {
                'gig': gig,
                'venue': venue,
            }
        )


class AceptGig(View):
    """class to change the status of the gig to Acepted"""

    def post(self, request, slug, *args, **kwargs):
        """Post the changes on database"""

        gig = get_object_or_404(Gig, slug=slug)
        venue = gig.venue

        gig.status = 1
        gig.save()

        return render(
            request, 'gig_details.html',
            {
                'gig': gig,
                'venue': venue,
            }
        )


class RefuseGig(View):
    """class to change status to Refused"""

    def post(self, request, slug, *args, **kwargs):
        """Post the changes on database"""

        gig = get_object_or_404(Gig, slug=slug)

        gig.status = 2
        gig.save()

        return redirect('home')


class UpdateGig(View):
    """Class to handle the update gigs"""

    def get(self, request, slug, *args, **kwargs):
        """Method to display the pre-populated form to update"""

        gig = get_object_or_404(Gig, slug=slug)
        form = GigCreationForm(instance=gig)

        return render(
            request,
            'edit_gig.html',
            {
                'form': form,
                'gig': gig,
            }
            )
    
    def post(self, request, slug, *args, **kwargs):
        """Post the new values for the gig"""

        gig = get_object_or_404(Gig, slug=slug)
        form = GigCreationForm(request.POST, instance=gig)

        if form.is_valid():
            form.save()

        return redirect('home')