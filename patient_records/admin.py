from django.contrib import admin
from .models import Patient

# Customize the Patient model display in the admin interface
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'id_number', 'age', 'medical_aid_scheme')
    search_fields = ('first_name', 'surname', 'id_number')
    list_filter = ('race', 'gender', 'medical_aid_scheme')

# Register the Patient model with the custom admin interface
admin.site.register(Patient, PatientAdmin)
