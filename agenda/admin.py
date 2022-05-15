from django.contrib import admin
from .models import Gig
from .models import Venue


@admin.register(Gig)
class GigAdminManager(admin.ModelAdmin):
    """Class for gig at the admin page"""

    list_display = ('name', 'date', 'dj', 'venue', 'status')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Venue)
class VenueAdminManager(admin.ModelAdmin):
    """class for venues at the admin page"""

    list_display = ('name', 'address', 'city', 'contact')
    prepopulated_fields = {'slug': ('name',)}
