from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingGigsView.as_view(), name='home'),
]
