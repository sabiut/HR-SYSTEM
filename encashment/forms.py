from login.models import Leave_Balance, NewLeave, encashment
from django import forms
from django.contrib.auth.models import User


# user info
class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class leave_encashment_form(forms.ModelForm):
    class Meta:
        model = encashment
        fields = ['department', 'Todays_date', 'total_number_of_days']
        widgets = {
            'Todays_date': DateInput()
        }


class director_authorize_encashment_form(forms.ModelForm):
    class Meta:
        model = encashment
        fields = ['approval_status', 'Authorize_by_Commissioner', 'Authorized_Date']
        widgets = {
            'Authorized_Date': DateInput()
        }


class processing_encashment_form(forms.ModelForm):
    class Meta:
        model = encashment
        fields = ['total_number_of_days', 'paid_amount', 'processing', 'payment_date']
        widgets = {
            'payment_date': DateInput()
        }
