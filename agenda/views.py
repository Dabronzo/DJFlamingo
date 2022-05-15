from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import View


class LandingGigsView(View):
    """View class to handle the gigs list or the landing page"""

    def get(self, request, *args, **kwargs):

        logged_in = self.request.user
        if logged_in.id is None:
            return render(
                request, 'landing.html'
                )
        elif logged_in.is_superuser:
            return render(
                request, 'staff.html'
            )
        else:
            return render(
                request, 'index.html'
            )


