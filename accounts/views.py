from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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
            # messages.success(request, (f"Welcome back {user.user_name}"))
            print("Entered")
            return redirect('home')

        else:
            messages.error(request,  ("An error ocurred with the login, please try again."))
            print("Error")
            return render(request, 'login')


class LogoutView(View):
    """View class for logout"""

    def get(self, request):
        """method for logut"""
        logout(request)
        return redirect('home')
