from django.contrib import admin

# Register your models here.
from .models import Patient, TravelHistory

admin.site.register(Patient)
admin.site.register(TravelHistory)