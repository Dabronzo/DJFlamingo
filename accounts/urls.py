from . import views
from django.urls import path

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrateUser.as_view(), name='register'),
    path('all_users', views.ViewAllDj.as_view(), name='all_users'),
]
