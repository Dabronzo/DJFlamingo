from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingGigsView.as_view(), name='home'),
    path('create_gig', views.CreateGigForm.as_view(), name='create_gig'),
]
