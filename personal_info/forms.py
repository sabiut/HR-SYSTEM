from django import forms
from django.contrib.auth.models import User

from login.models import Profile, emergency, Family_and_Dependants, education_history, Job_History


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Gender', 'Marital_Status', 'date_of_birth', 'Address', 'job_title', 'join_Date',
                  'Account_number', 'department',
                  'employee_code')


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = emergency
        fields = (
            'contact_name', 'Relationship', 'Address', 'City', 'Home_Phone', 'Mobile_Phone')


class Family_and_DependantsForm(forms.ModelForm):
    class Meta:
        model = Family_and_Dependants
        fields = (
            'contact_name', 'Relationship', 'Birth_Date', 'Gender', 'Marital_Status', 'Address', 'Home_Phone')


class add_ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'user', 'Gender', 'Marital_Status', 'date_of_birth', 'Address', 'job_title', 'join_Date',
            'Bank_name', 'Account_number',
            'department',
            'employee_code')

        widgets = {
            'date_of_birth': DateInput(), 'join_Date': DateInput()
        }


class add_education_history(forms.ModelForm):
    class Meta:
        model = education_history
        fields = (
            'user', 'education_level', 'Institution', 'Major', 'start_date', 'end_date', 'Country', 'Last_Education')

        widgets = {
            'start_date': DateInput(), 'end_date': DateInput()
        }


class add_staff_emergency_Form(forms.ModelForm):
    class Meta:
        model = emergency
        fields = (
            'user', 'contact_name', 'Relationship', 'Address', 'City', 'Home_Phone', 'Mobile_Phone')


class add_family_dependant_Form(forms.ModelForm):
    class Meta:
        model = Family_and_Dependants
        fields = ('user', 'contact_name', 'Relationship', 'Birth_Date', 'Gender', 'Marital_Status', 'Home_Phone',
                  'Address')

        widgets = {
            'Birth_Date': DateInput()
        }


class add_job_history_Form(forms.ModelForm):
    class Meta:
        model = Job_History
        fields = ('user', 'Company_name', 'Address', 'start_date', 'end_date', 'Position', 'Responsibilities')

        widgets = {
            'start_date': DateInput(), 'end_date': DateInput()
        }
