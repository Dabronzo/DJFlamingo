from django.contrib import admin
from .models import NewDjUser



@admin.register(NewDjUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_name', 'is_staff', 'join_date')
