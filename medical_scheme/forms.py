from django.contrib.auth.models import User
#from housing_loan.models import *
from django import forms

from medical_scheme.models import medical_details


class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class medical_form(forms.ModelForm):
    class Meta:
        model = medical_details
        fields = ['medical_check_type', 'Total_Cost', 'attached_receipt', 'date_you_see_the_doctor', 'year',
                  'I_hereby_declare_that_all_the_information_provided_above_is_true']

        widgets = {'date_you_see_the_doctor': DateInput()

                   }


class FC_process_Form(forms.ModelForm):
    class Meta:
        model = medical_details
        fields = ['Status', 'process_date']

        widgets = {'process_date': DateInput()

                   }
