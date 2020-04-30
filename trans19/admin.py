from django.contrib import admin
from .models import Patient, Location, Visit


class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Location Name', {'fields': ['location_name']}),
        ('District', {'fields': ['district']}),
        ('Address', {'fields': ['address']}),
        ('X Coord', {'fields': ['x_coord']}),
        ('Y Coord', {'fields': ['y_coord']}),
    ]
    list_display = ('location_name', 'district')
    list_filter = ['district']


class VisitInline(admin.StackedInline):
    model = Visit
    extra = 0


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['patient_name']}),
        ('ID number', {'fields': ['patient_id']}),
        ('Date of birth', {'fields': ['date_of_birth']}),
        ('Date case confirmed', {'fields': ['date_case_confirmed']}),
        ('Case number', {'fields': ['case_number']}),
    ]
    inlines = [VisitInline]
    search_fields = ['case_number']
    list_display = ('case_number', 'patient_name')


admin.site.register(Patient, PatientAdmin)
admin.site.register(Location, LocationAdmin)
