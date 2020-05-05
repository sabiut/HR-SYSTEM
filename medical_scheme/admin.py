from django.contrib import admin

# Register your models here.
from medical_scheme.models import medical_details, medical_entitlement

admin.site.register(medical_details)
admin.site.register(medical_entitlement)
