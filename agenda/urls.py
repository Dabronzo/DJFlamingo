from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingGigsView.as_view(), name='home'),
    path('create_gig', views.CreateGig.as_view(), name='create_gig'),
    path('create_venue', views.CreateVenue.as_view(), name='create_venue'),
]
