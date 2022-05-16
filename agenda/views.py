from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Gig


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
            return render(
                request, 'index.html'
            )


class CreateGigForm(View):
    """View Class to show the fomr to create a new gig"""

    def get(self, request, *args, **kwargs):

        return render(
            request, 'create_gig.html'
        )
