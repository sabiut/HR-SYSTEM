from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


# Signal
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True, default=None)
    gen = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Gender = models.CharField(max_length=100, choices=gen, blank=False, default='')

    marital = (
        ('Single', 'Single'),
        ('Married', 'Married'),
    )
    Marital_Status = models.CharField(max_length=100, choices=marital, blank=False, default='')
    dp = (
        ('Finance', 'Finance'),
        ('ICT', 'ICT'),
        ('Research', 'Research'),
        ('Marketing', 'Marketing'),
    )

    department = models.CharField(max_length=100, choices=dp, blank=False, )
    Address = models.CharField(max_length=100, null=True, blank=True, default=None)
    BN = ed = (
        ('ANZ', 'ANZ'),
        ('Westpac', 'Westpac'),
        ('ASB', 'ASB'),

    )
    Bank_name = models.CharField(max_length=100, choices=BN, null=True, blank=True, default=None)
    Account_number = models.CharField(max_length=100, null=True, blank=True, default=None)
    employee_code = models.CharField(max_length=100, default='')
    organization = models.CharField(max_length=100, null=True, blank=True, default=None)
    job_title = models.CharField(max_length=100, blank=True, null=True, default=None)
    join_Date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.first_name


class education_history(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    ed = (
        ('PHD', 'PHD'),
        ('Masters', 'Masters'),
        ('Post Graduate', 'Post Graduate'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
    )
    education_level = models.CharField(max_length=100, choices=ed, blank=True, null=True, default=None)
    Institution = models.CharField(max_length=100, blank=True, null=True, default=None)
    Major = models.CharField(max_length=100, blank=True, null=True, default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    Country = models.CharField(max_length=100, blank=True, null=True, default=None)
    Last_Education = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.user.first_name


class emergency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    Relationship = models.CharField(max_length=100, blank=True, null=True, default=None)
    Address = models.CharField(max_length=100, blank=True, null=True, default=None)
    City = models.CharField(max_length=100, blank=True, null=True, default=None)
    Home_Phone = models.CharField(max_length=100, blank=True, null=True, default=None)
    Mobile_Phone = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.user.first_name


class Family_and_Dependants(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    Relationship = models.CharField(max_length=100, blank=True, null=True, default=None)
    Birth_Date = models.DateField(null=True, blank=True, default=None)
    gen = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Gender = models.CharField(max_length=100, choices=gen, blank=False, default='')

    marital = (
        ('Single', 'Single'),
        ('Married', 'Married'),
    )
    Marital_Status = models.CharField(max_length=100, choices=marital, blank=False, default='')
    Address = models.CharField(max_length=100, blank=True, null=True, default=None)
    Home_Phone = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.user.first_name


class Job_History(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    Address = models.CharField(max_length=100, blank=True, null=True, default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    Position = models.CharField(max_length=100, blank=True, null=True, default=None)
    Responsibilities = models.TextField(max_length=1000)

    def __str__(self):
        return self.user.first_name


def create_profile(sender, **kwargs):
    user = kwargs["instance"]

    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_emergency = emergency(user=user)
        user_profile.save()
        user_emergency.save()


post_save.connect(create_profile, sender=User)


class Leave_Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    Leave_current_balance = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.first_name


class monthly_entitlement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    leave_balances = models.ManyToManyField(Leave_Balance)
    entitlement = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.first_name


class month_and_year(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    Month = models.CharField(max_length=100, default="", null=True)
    Year = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.first_name


class NewLeave(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    leave_balances = models.ManyToManyField(Leave_Balance)
    leave = (
        ('annual', 'annual'),

    )

    Leave_type = models.CharField(max_length=100, choices=leave, blank=False, default='annual')
    dp = (
        ('Finance', 'Finance'),
        ('ICT', 'ICT'),
        ('Research', 'Research'),
        ('Marketing', 'Marketing'),
    )

    department = models.CharField(max_length=100, choices=dp, blank=False, )
    Start_Date = models.DateField(null=True, blank=False)
    End_Date = models.DateField(null=True, blank=False)
    Total_working_days = models.FloatField(null=True, blank=False)
    Reason = models.TextField(max_length=1000, null=True, blank=False)
    Aut = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    Manager_Authorization_Status = models.CharField(max_length=100, choices=Aut, default='Pending', blank=False)
    Authorized_by_Manager = models.CharField(max_length=100, default='', blank=False)
    Authorised_Date = models.DateField(null=True, blank=False)
    DirAuth = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    Director_Authorization_Status = models.CharField(max_length=100, choices=DirAuth, default='Pending', blank=False)
    Authorized_by_Director = models.CharField(max_length=100, default='', blank=False)
    Date_Authorized = models.DateField(null=True, blank=False)
    arc = (
        ('', ''),
        ('Archived', 'Archived'),

    )
    Archived = models.CharField(max_length=100, choices=arc, default='', blank=False)

    def __str__(self):
        return self.user.first_name


class Sick_leave_balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sick_leave_balance = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.first_name


class Sick_leave_month_year(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yearly_balance = models.FloatField(null=True, blank=True, default=None)

    mnt = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'March'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),

    )

    Month = models.CharField(max_length=100, choices=mnt, blank=False)
    yr = (
        ('2051', '2051'),
        ('2050', '2050'),
        ('2049', '2049'),
        ('2048', '2048'),
        ('2047', '2047'),
        ('2046', '2046'),
        ('2045', '2045'),
        ('2044', '2044'),
        ('2043', '2043'),
        ('2042', '2042'),
        ('2041', '2041'),
        ('2040', '2040'),
        ('2039', '2039'),
        ('2038', '2038'),
        ('2037', '2037'),
        ('2036', '2036'),
        ('2035', '2035'),
        ('2034', '2034'),
        ('2033', '2033'),
        ('2032', '2032'),
        ('2031', '2031'),
        ('2030', '2030'),
        ('2029', '2029'),
        ('2028', '2028'),
        ('2027', '2027'),
        ('2026', '2026'),
        ('2025', '2025'),
        ('2024', '2024'),
        ('2023', '2010'),
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('2019', '2019'),

    )

    Year = models.CharField(max_length=100, choices=yr, blank=False)

    def __str__(self):
        return self.user.first_name


class SickLeave(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    sick_leave_balances = models.ManyToManyField(Sick_leave_balance)
    leave = (
        ('sick', 'sick'),

    )

    Leave_type = models.CharField(max_length=100, choices=leave, blank=False, default='sick')
    dp = (
        ('Finance', 'Finance'),
        ('ICT', 'ICT'),
        ('Research', 'Research'),
        ('Marketing', 'Marketing'),
    )
    Todays_Date = models.DateField(null=True, blank=False)
    department = models.CharField(max_length=100, choices=dp, blank=False, )
    Date_illness_began = models.DateField(null=True, blank=False)
    Date_illness_end = models.DateField(null=True, blank=False)
    Total_working_days = models.FloatField(null=True, blank=False)
    Brief_explanation_of_illness = models.TextField(max_length=1000, null=True, blank=False)
    medical_certification = models.FileField(upload_to='medical_sick_sheet/pdf/')

    Aut = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    Manager_Authorization_Status = models.CharField(max_length=100, choices=Aut, default='Pending', blank=False)
    Authorized_by_Manager = models.CharField(max_length=100, default='', blank=False)
    Authorised_Date = models.DateField(null=True, blank=False)
    DirAuth = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    Director_Authorization_Status = models.CharField(max_length=100, choices=DirAuth, default='Pending', blank=False)
    Authorized_by_Director = models.CharField(max_length=100, default='', blank=False)
    Date_Authorized = models.DateField(null=True, blank=False)
    arc = (
        ('', ''),
        ('Archived', 'Archived'),

    )
    Archived = models.CharField(max_length=100, choices=arc, default='', blank=False)

    def __str__(self):
        return self.user.first_name


class encashment(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    dp = (
        ('Finance', 'Finance'),
        ('ICT', 'ICT'),
        ('Research', 'Research'),
        ('Marketing', 'Marketing'),
    )
    department = models.CharField(max_length=100, choices=dp, blank=False, default='')
    Todays_date = models.DateField()
    total_number_of_days = models.FloatField()
    paid_amount = models.FloatField(null=True)
    processed_date = models.DateField(null=True, blank=False)
    status = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),

    )
    approval_status = models.CharField(max_length=100, choices=status, default='Pending', blank=False)
    Authorize_by_Commissioner = models.CharField(max_length=100, null=True)
    Authorized_Date = models.DateField(null=True, blank=False)
    review = (
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),

    )
    processing = models.CharField(max_length=100, choices=review, default="Processing", blank=False)
    payment_date = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.user.first_name


class staff_loan(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    dp = (
        ('Finance', 'Finance'),
        ('ICT', 'ICT'),
        ('Research', 'Research'),
        ('Marketing', 'Marketing'),
    )

    department = models.CharField(max_length=100, choices=dp, blank=False, )
    Post_title = models.CharField(max_length=100)
    type = (
        ('Schools Fees', 'School Fees'),
        ('Medical', 'Medical'),
        ('Death', 'Death'),
        ('Marriage', 'Marriage'),

    )
    Loan_type = models.CharField(max_length=100, choices=type, blank=False, )
    Others = models.CharField(max_length=100, blank=True)
    Requested_Amount = models.FloatField()
    Interest_5_percent = models.FloatField()
    Repayment_Amount = models.FloatField()
    Date_of_repayment_commencement = models.DateField()
    I_hereby_declare_that_all_the_information_provided_above_is_true = models.BooleanField(default=True, null=False)
    Launch_Date = models.DateField()
    review_status = (
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),

    )
    review_status = models.CharField(max_length=100, choices=review_status, default='Pending', blank=False)
    committee_comments = models.TextField(max_length=200, default='')
    status = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),

    )
    approval_status = models.CharField(max_length=100, choices=status, blank=False, default='Pending')
    Authorize_by_Commissioner = models.CharField(max_length=100, null=True)
    comments = models.TextField()
    Authorized_Date = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.user.first_name
