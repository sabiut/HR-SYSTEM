# Generated by Django 3.0 on 2020-03-02 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_Balance',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Leave_current_balance', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sick_leave_balance',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sick_leave_balance', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff_loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('ICT', 'ICT'), ('Research', 'Research'), ('Marketing', 'Marketing')], max_length=100)),
                ('Post_title', models.CharField(max_length=100)),
                ('Loan_type', models.CharField(choices=[('Schools Fees', 'School Fees'), ('Medical', 'Medical'), ('Death', 'Death'), ('Marriage', 'Marriage')], max_length=100)),
                ('Others', models.CharField(blank=True, max_length=100)),
                ('Requested_Amount', models.FloatField()),
                ('Interest_5_percent', models.FloatField()),
                ('Repayment_Amount', models.FloatField()),
                ('Date_of_repayment_commencement', models.DateField()),
                ('I_hereby_declare_that_all_the_information_provided_above_is_true', models.BooleanField(default=True)),
                ('Launch_Date', models.DateField()),
                ('review_status', models.CharField(choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed')], default='Pending', max_length=100)),
                ('committee_comments', models.TextField(default='', max_length=200)),
                ('approval_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('Authorize_by_Commissioner', models.CharField(max_length=100, null=True)),
                ('comments', models.TextField()),
                ('Authorized_Date', models.DateField(null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SickLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_type', models.CharField(choices=[('sick', 'sick')], default='sick', max_length=100)),
                ('Todays_Date', models.DateField(null=True)),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('ICT', 'ICT'), ('Research', 'Research'), ('Marketing', 'Marketing')], max_length=100)),
                ('Date_illness_began', models.DateField(null=True)),
                ('Date_illness_end', models.DateField(null=True)),
                ('Total_working_days', models.FloatField(null=True)),
                ('Brief_explanation_of_illness', models.TextField(max_length=1000, null=True)),
                ('medical_certification', models.FileField(upload_to='medical_sick_sheet/pdf/')),
                ('Manager_Authorization_Status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('Authorized_by_Manager', models.CharField(default='', max_length=100)),
                ('Authorised_Date', models.DateField(null=True)),
                ('Director_Authorization_Status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('Authorized_by_Director', models.CharField(default='', max_length=100)),
                ('Date_Authorized', models.DateField(null=True)),
                ('Archived', models.CharField(choices=[('', ''), ('Archived', 'Archived')], default='', max_length=100)),
                ('sick_leave_balances', models.ManyToManyField(to='login.Sick_leave_balance')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sick_leave_month_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearly_balance', models.FloatField(blank=True, default=None, null=True)),
                ('Month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'March'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=100)),
                ('Year', models.CharField(choices=[('2051', '2051'), ('2050', '2050'), ('2049', '2049'), ('2048', '2048'), ('2047', '2047'), ('2046', '2046'), ('2045', '2045'), ('2044', '2044'), ('2043', '2043'), ('2042', '2042'), ('2041', '2041'), ('2040', '2040'), ('2039', '2039'), ('2038', '2038'), ('2037', '2037'), ('2036', '2036'), ('2035', '2035'), ('2034', '2034'), ('2033', '2033'), ('2032', '2032'), ('2031', '2031'), ('2030', '2030'), ('2029', '2029'), ('2028', '2028'), ('2027', '2027'), ('2026', '2026'), ('2025', '2025'), ('2024', '2024'), ('2023', '2010'), ('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=100)),
                ('Marital_Status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], default='', max_length=100)),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('ICT', 'ICT'), ('Research', 'Research'), ('Marketing', 'Marketing')], max_length=100)),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Bank_name', models.CharField(blank=True, choices=[('ANZ', 'ANZ'), ('Westpac', 'Westpac'), ('ASB', 'ASB')], default=None, max_length=100, null=True)),
                ('Account_number', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('employee_code', models.CharField(default='', max_length=100)),
                ('organization', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('job_title', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('join_Date', models.DateField(blank=True, default=None, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_type', models.CharField(choices=[('annual', 'annual')], default='annual', max_length=100)),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('ICT', 'ICT'), ('Research', 'Research'), ('Marketing', 'Marketing')], max_length=100)),
                ('Start_Date', models.DateField(null=True)),
                ('End_Date', models.DateField(null=True)),
                ('Total_working_days', models.FloatField(null=True)),
                ('Reason', models.TextField(max_length=1000, null=True)),
                ('Manager_Authorization_Status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('Authorized_by_Manager', models.CharField(default='', max_length=100)),
                ('Authorised_Date', models.DateField(null=True)),
                ('Director_Authorization_Status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('Authorized_by_Director', models.CharField(default='', max_length=100)),
                ('Date_Authorized', models.DateField(null=True)),
                ('Archived', models.CharField(choices=[('', ''), ('Archived', 'Archived')], default='', max_length=100)),
                ('leave_balances', models.ManyToManyField(to='login.Leave_Balance')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthly_entitlement',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('entitlement', models.FloatField(blank=True, default=None, null=True)),
                ('leave_balances', models.ManyToManyField(to='login.Leave_Balance')),
            ],
        ),
        migrations.CreateModel(
            name='month_and_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.CharField(default='', max_length=100, null=True)),
                ('Year', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('Position', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Responsibilities', models.TextField(max_length=1000)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Family_and_Dependants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Relationship', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Birth_Date', models.DateField(blank=True, default=None, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=100)),
                ('Marital_Status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], default='', max_length=100)),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Home_Phone', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='encashment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('ICT', 'ICT'), ('Research', 'Research'), ('Marketing', 'Marketing')], default='', max_length=100)),
                ('Todays_date', models.DateField()),
                ('total_number_of_days', models.FloatField()),
                ('paid_amount', models.FloatField(null=True)),
                ('processed_date', models.DateField(null=True)),
                ('approval_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('Authorize_by_Commissioner', models.CharField(max_length=100, null=True)),
                ('Authorized_Date', models.DateField(null=True)),
                ('processing', models.CharField(choices=[('Processing', 'Processing'), ('Completed', 'Completed')], default='Processing', max_length=100)),
                ('payment_date', models.DateField(null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Relationship', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('City', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Home_Phone', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Mobile_Phone', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='education_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(blank=True, choices=[('PHD', 'PHD'), ('Masters', 'Masters'), ('Post Graduate', 'Post Graduate'), ('Bachelor Degree', 'Bachelor Degree'), ('Diploma', 'Diploma'), ('Certificate', 'Certificate')], default=None, max_length=100, null=True)),
                ('Institution', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Major', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('Country', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Last_Education', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]