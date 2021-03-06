# Generated by Django 3.2.13 on 2022-05-15 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=120, verbose_name='City')),
                ('website', models.URLField(verbose_name='Venue Website')),
                ('contact', models.CharField(max_length=200, verbose_name='Contact Name and Phone')),
                ('additional_info', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Proposal'), (1, 'Aproved'), (2, 'Rejected'), (3, 'Cancelled')], default=0)),
                ('date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('time_start', models.TimeField()),
                ('time_duration', models.TimeField()),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total fees')),
                ('is_payed', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('dj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gig_event', to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gig_venue', to='agenda.venue')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
