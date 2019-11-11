from django.contrib import admin
from .models import Profile
# Register your models here.
class AdminProfile(admin.ModelAdmin):
    ordering = ['-id']

admin.site.register(Profile,AdminProfile)
