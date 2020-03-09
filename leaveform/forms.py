from django import forms
from django.contrib.auth.models import User


# user info

from login.models import Leave_Balance, NewLeave, Profile


class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class balance_form(forms.ModelForm):
    class Meta:
        model = Leave_Balance
        fields = ['Leave_current_balance', ]


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class application_form(forms.ModelForm):
    class Meta:
        model = NewLeave
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}
        fields = ['department', 'Leave_type', 'Total_working_days', 'Start_Date', 'End_Date', 'Reason', ]
        widgets = {
            'Start_Date': DateInput(), 'End_Date': DateInput()
        }
