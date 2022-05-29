from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from agenda.models import Gig
from .forms import RegistrationForm
from .models import NewDjUser


class LoginView(View):
    """View class to login"""

    def get(self, request):
        """Render login page"""

        return render(
            request, 'login.html'
        )

    def post(self, request):
        """Post for Login"""

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, (f"Welcome back {user.user_name}"))
            print("Entered")
            return redirect('home')

        else:
            messages.error(request,  (
                "An error ocurred with the login, please try again."
                ))
            return render(request, 'login.html')


class LogoutView(View):
    """View class for logout"""

    def get(self, request):
        """method for logut"""
        logout(request)
        return redirect('home')


class RegistrateUser(View):
    """Class view for new users registration"""

    def get(self, request, *args, **kwargs):

        form = RegistrationForm()

        return render(
            request, 'register.html',
            {
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        """Post method to authenticate"""
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.info(request, (
                "Success! You are registered on Flamingo"
            ))

            return redirect('home')
        else:
            messages.error(request, (
                "Something went wrong, please try it again."
            ))
            return render(
                request,
                'register.html', {
                    'form': form
                }
            )


class ViewAllDj(View):
    """Class view to display a table with all the
    registered dj"""

    def get(self, request, *args, **kwargs):
        """Display all users"""

        logged_in = self.request.user
        if logged_in.is_superuser:
            queryset = NewDjUser.objects.all().order_by('join_date')
            return render(
                request, 'all_users.html',
                {
                    'all_users': queryset,
                }
            )
        else:
            return redirect('home')


class DetailsDJView(View):
    """Render a page with details of a specific dj"""

    def get(self, request, username, *args, **kwargs):
        """Query the dj selected and render"""
        logged_in = self.request.user
        if logged_in.is_superuser:
            queryset = NewDjUser.objects.all()
            dj = get_object_or_404(queryset, user_name=username)
            gigs = Gig.objects.all()
            gigs_assigned = 0
            for gig in gigs:
                if gig.dj.user_name == dj.user_name:
                    gigs_assigned += 1

            return render(
                request, 'user_details.html',
                {
                    'dj': dj,
                    'gigs_assigned': gigs_assigned,
                }
            )

        else:
            return redirect('home')


class DeleteUser(View):
    """Delete a selected user"""

    def post(self, request, username, *args, **kwargs):
        """Delete from the database"""
        if self.request.user.is_superuser:
            dj = get_object_or_404(NewDjUser, user_name=username)
            messages.info(request, (
                f"User {dj.user_name} was deleted!"
            ))
            dj.delete()

            return redirect('home')
