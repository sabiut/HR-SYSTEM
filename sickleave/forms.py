from django import forms
from django.contrib.auth.models import User

from login.models import SickLeave, Sick_leave_month_year


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class sick_leave_form(forms.ModelForm):
    class Meta:
        model = SickLeave
        fields = ['department', 'Todays_Date', 'Leave_type', 'Total_working_days', 'Date_illness_began',
                  'Date_illness_end',
                  'Brief_explanation_of_illness', 'medical_certification', ]
        widgets = {
            'Todays_Date': DateInput(), 'Date_illness_began': DateInput(), 'Date_illness_end': DateInput()
        }


class update_sick_leave_form(forms.ModelForm):
    class Meta:
        model = Sick_leave_month_year
        fields = ['user', 'yearly_balance', 'Month', 'Year']
