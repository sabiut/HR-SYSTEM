from django import forms
from django.contrib.auth.models import User

from login.models import Leave_Balance


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class update_leave_balance_form(forms.ModelForm):
    class Meta:
        model = Leave_Balance
        fields = ['Leave_current_balance']
