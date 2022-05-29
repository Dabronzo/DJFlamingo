from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator
from .models import Gig
from .forms import GigCreationForm, VenueCreationForm
from .filters import GigFilter


class AllGigsHistory(View):
    """Admin view to display table with a view of completed gigs"""

    def get(self, request, *args, **kwargs):
        """Query the gigs and display the template"""
        if self.request.user.is_superuser:
            queryset = Gig.objects.all().order_by('date')
            gigs_history = []
            for gig in queryset:
                if gig.days_to < 0:
                    gigs_history.append(gig)

            return render(
                request,
                'gigs_history.html',
                {
                    'gigs_history': gigs_history,
                }
            )
        else:
            return redirect('home')


class MyGigsHistory(View):
    """User class view the passed gigs info"""

    def get(self, request, *args, **kwargs):
        """Display template"""
        logged_in = self.request.user
        queryset = Gig.objects.filter(dj=logged_in).order_by('date')

        past_gigs = []
        for gig in queryset:
            if gig.days_to < 0:
                past_gigs.append(gig)

        return render(
            request, 'history.html',
            {
                'past_gigs': past_gigs,
            }
        )


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
    """Admin view Class to show the fomr to create a new gig"""

    def get(self, request, *args, **kwargs):

        if self.request.user.is_superuser:
            form = GigCreationForm()
            return render(
                request, 'create_gig.html',
                {
                    'form': form,
                }
            )
        else:
            return redirect('home')

    def post(self, request, *args, **kwargs):
        """Post Method to create gig"""

        form = GigCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, (
                "New gig created!"
            ))
            form.save()

            return redirect('home')
        else:
            messages.error(request, (
                "Oops something went wrong, try it again."
            ))
            return render(
                request, 'create_gig.html',
                {
                    'form': form,
                }
            )


class DeleteGig(View):
    """Admin view class to delete a gig from the database"""

    def post(self, request, slug, *args, **kwargs):
        """Post to delete"""

        if self.request.user.is_superuser:
            gig = get_object_or_404(Gig, slug=slug)
            messages.info(request, (
                "Gig deleted!"
            ))
            gig.delete()

            return redirect('home')


class CreateVenue(View):
    """Admin view class for the venue creation"""

    def get(self, request, *args, **kwargs):
        """Get to show the form and template"""

        if self.request.user.is_superuser:
            form = VenueCreationForm()

            return render(
                request, 'create_venue.html',
                {
                    'form': form,
                }
            )
        else:
            return redirect('home')

    def post(self, request, *args, **kwargs):
        """Post to create a venue"""

        form = VenueCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, (
                "New venue created!"
            ))
            form.save()

            return redirect('home')


class GigDetails(View):
    """User and Admin class view to the details of a specific gig"""

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
    """User class to change the status of the gig to acepted"""

    def post(self, request, slug, *args, **kwargs):
        """Post the changes on database"""

        gig = get_object_or_404(Gig, slug=slug)
        venue = gig.venue

        gig.status = 1
        messages.info(request, (
            "Gig proposal accepted!"
        ))
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
        messages.info(request, (
            "Gig refused!"
        ))
        gig.save()

        return redirect('home')


class UpdateGig(View):
    """Admin class to handle the update gigs"""

    def get(self, request, slug, *args, **kwargs):
        """Method to display the pre-populated form to update"""

        if self.request.user.is_superuser:
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
        else:
            return redirect('home')

    def post(self, request, slug, *args, **kwargs):
        """Post the new values for the gig"""

        gig = get_object_or_404(Gig, slug=slug)
        form = GigCreationForm(request.POST, instance=gig)

        if form.is_valid():
            messages.success(request, (
                "Gig updated!"
            ))
            form.save()
            return redirect('home')
        else:
            messages.error(request, (
                "Oops, something went worng."
            ))
            return render(
                request,
                'edit_gig.html',
                {
                    'form': form,
                    'gig': gig,
                }
            )
