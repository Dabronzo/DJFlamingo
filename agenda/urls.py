from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path

urlpatterns = [
    path(
        '',
        views.LandingGigsView.as_view(),
        name='home'
        ),
    path(
        'create_gig',
        views.CreateGig.as_view(),
        name='create_gig'
        ),
    path(
        'create_venue',
        views.CreateVenue.as_view(),
        name='create_venue'
        ),
    path(
        'details/<slug:slug>',
        login_required(views.GigDetails.as_view()),
        name='gig_details'
        ),
    path(
        'update/<slug:slug>',
        views.UpdateGig.as_view(),
        name='update_gig'
        ),
    path(
        'accept/<slug:slug>',
        login_required(views.AceptGig.as_view()),
        name='accept'
        ),
    path(
        'refuse/<slug:slug>',
        login_required(views.RefuseGig.as_view()),
        name='refuse'
        ),
    path(
        'delete_gig/<slug:slug>',
        views.DeleteGig.as_view(),
        name='delete'
        ),
    path(
        'history',
        login_required(views.MyGigsHistory.as_view()),
        name='history'
        ),
    path(
        'gigs_history',
        views.AllGigsHistory.as_view(),
        name='gigs_history'
        ),
]
