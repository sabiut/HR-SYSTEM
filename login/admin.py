from django.contrib import admin
from django.contrib.admin import site

from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Leave_Balance)
admin.site.register(NewLeave)
admin.site.register(monthly_entitlement)
admin.site.register(month_and_year)
admin.site.register(education_history)
admin.site.register(emergency)
admin.site.register(Family_and_Dependants)
admin.site.register(Job_History)
admin.site.register(encashment)

