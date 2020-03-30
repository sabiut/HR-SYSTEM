from django import forms

from login.models import *


class add_to_archive_form(forms.ModelForm):
    class Meta:
        model = NewLeave
        fields = ['Archived', ]


class update_entitlement_form(forms.ModelForm):
    class Meta:
        model = month_and_year
        fields = ['user', 'Month', 'Year']
