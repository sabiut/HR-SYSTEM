from login.models import NewLeave, SickLeave
from django import forms
from django.contrib.auth.models import User


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class ManagerForm(forms.ModelForm):
    class Meta:
        model = NewLeave
        fields = ('Manager_Authorization_Status', 'Authorized_by_Manager', 'Authorised_Date',)
        widgets = {
            'Authorised_Date': DateInput()
        }


class DirectorForm(forms.ModelForm):
    class Meta:
        model = NewLeave
        fields = ('Director_Authorization_Status', 'Authorized_by_Director', 'Date_Authorized',)
        widgets = {
            'Date_Authorized': DateInput()
        }


class Manager_approve_sick_Form(forms.ModelForm):
    class Meta:
        model = SickLeave
        fields = ('Manager_Authorization_Status', 'Authorized_by_Manager', 'Authorised_Date',)
        widgets = {
            'Authorised_Date': DateInput()
        }
