from django import forms
from .models import *


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class add_holiday_form(forms.ModelForm):
    class Meta:
        model = holiday
        fields = ['day', 'date', 'holiday_name', 'holiday_type', 'comment']
        widgets = {
            'date': DateInput(),
        }

