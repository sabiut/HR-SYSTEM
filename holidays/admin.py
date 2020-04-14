from django.contrib import admin

# Register your models here.
from django.contrib.admin import site

from . models import holiday
admin.site.register(holiday)
