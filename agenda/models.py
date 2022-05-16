from django.db import models
from accounts.models import NewDjUser
from datetime import date
from django.template.defaultfilters import slugify

STATUS = ((0, 'Proposal'), (1, 'Aproved'), (2, 'Rejected'), (3, 'Cancelled'))


class Venue(models.Model):
    """Class table for the venues"""

    name = models.CharField('Venue Name', max_length=120, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField('City', max_length=120)
    website = models.URLField('Venue Website', blank=True)
    contact = models.CharField('Contact Name and Phone', max_length=200)
    additional_info = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        """Save method to create venues"""
        self.slug = slugify(self.name)
        super(Venue, self).save(*args, **kwargs)


class Gig(models.Model):
    """Class table for the gigs"""

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    time_start = models.TimeField()
    time_duration = models.CharField('Gig total time', max_length=50)
    dj = models.ForeignKey(
        NewDjUser, on_delete=models.CASCADE, related_name='gig_event'
        )
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='gig_venue'
    )
    fees = models.DecimalField('Total fees', max_digits=10, decimal_places=2)
    is_payed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    @property
    def days_to(self):
        """Function to return how many days
        until the gig"""

        today = date.today()
        days_till_gig = (self.date - today)
        return days_till_gig

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"Gig on {self.date} at {self.venue.name} assined to {self.dj.user_name}"

    def save(self, *args, **kwargs):
        """Save method to create a new gig"""
        self.slug = slugify(self.name)
        super(Gig, self).save(*args, **kwargs)
