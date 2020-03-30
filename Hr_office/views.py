from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# archived leaves
from django.template.context_processors import csrf
from djqscsv import render_to_csv_response

from Hr_office.forms import add_to_archive_form, update_entitlement_form
from leaveform.forms import application_form, User_form
from login.models import *
from django.db.models import Sum

import csv

from sickleave.forms import sick_leave_form


@login_required(login_url='home')
def update_leave_form(request, staffs_id):
    if request.method == 'POST':
        user_form = User_form(request.POST, instance=request.user)
        get_staff_id = NewLeave.objects.get(id=staffs_id)
        name = get_staff_id.user
        form = application_form(request.POST, instance=get_staff_id)
        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            new_leave = form.save(commit=False)
            new_leave.user = user
            new_leave.save()
            return render(request, 'update_application_thanks.html', {'name': name})

    else:
        get_staff_id = NewLeave.objects.get(id=staffs_id)
        form = application_form(instance=get_staff_id)
        user_form = User_form(instance=request.user)

    return render(request, 'update_leave_application_form.html', locals())


@login_required(login_url='home')
def update_sick_leave_form(request, staffs_id):
    if request.method == 'POST':
        user_form = User_form(request.POST, instance=request.user)
        get_staff_id = SickLeave.objects.get(id=staffs_id)
        name = get_staff_id.user
        form = sick_leave_form(request.POST, instance=get_staff_id)
        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            new_leave = form.save(commit=False)
            new_leave.user = user
            new_leave.save()
            return render(request, 'update_application_thanks.html', {'name': name})

    else:
        get_staff_id = SickLeave.objects.get(id=staffs_id)
        form = sick_leave_form(instance=get_staff_id)
        user_form = User_form(instance=request.user)

    return render(request, 'update_leave_application_form.html', locals())




@login_required(login_url='home')
def archivedLeaves(request):
    archives_leaves = NewLeave.objects.filter(Archived='Archived',
                                              Director_Authorization_Status='Approved',
                                              Manager_Authorization_Status='Approved')
    return render(request, 'archived_leaves.html', locals())


@login_required(login_url='home')
def allStaffLeaves(request):
    all_leaves = NewLeave.objects.all()
    return render(request, 'all_leaves.html', locals())


@login_required(login_url='home')
def approvedLeaves(request):
    approved_leaves = NewLeave.objects.filter(Manager_Authorization_Status='Approved',
                                              Director_Authorization_Status='Approved')
    return render(request, 'approved_leaves.html', locals())


@login_required(login_url='home')
def rejectedLeaves(request):
    rejected_leaves = NewLeave.objects.filter(Manager_Authorization_Status='Rejected',
                                              Director_Authorization_Status='Rejected')
    return render(request, 'rejected_leaves.html', locals())


@login_required(login_url='home')
def hr_archive_leave(request, leave_id):
    if request.method == 'POST':
        leaveID = NewLeave.objects.get(id=leave_id)
        archive_form = add_to_archive_form(request.POST, instance=leaveID)
        if archive_form.is_valid():
            archive_form.save()
            return HttpResponse('You have successfully archived the leave')

    else:
        leaveID = NewLeave.objects.get(id=leave_id)
        archive_form = add_to_archive_form(instance=leaveID)
    return render(request, 'hr_archive_leave.html', {'form': archive_form})


@login_required(login_url='home')
def staff_balances(request):
    staff_balance = month_and_year.objects.all()
    return render(request, 'staff_entitlements.html', locals())


@login_required(login_url='home')
def update_monthly_entitlement(request):
    if request.POST:
        entitlement_form = update_entitlement_form(request.POST)
        if entitlement_form.is_valid():
            my_field = entitlement_form.cleaned_data['user']
            calculate_monthly_entitlement(my_field)
            entitlement_form.save()
            return HttpResponseRedirect('/staff_balances')
    else:
        entitlement_form = update_entitlement_form
    args = {}
    args.update(csrf(request))
    args['form'] = entitlement_form
    return render(request, 'update_entitlement_form.html', args)


def calculate_monthly_entitlement(get_id):
    get_id = get_id
    get_leave_balance_id = Leave_Balance.objects.get(user_id=get_id)
    get_entitlement_id = monthly_entitlement.objects.get(user_id=get_id)
    get_leave_balance_id.Leave_current_balance = get_leave_balance_id.Leave_current_balance + get_entitlement_id.entitlement
    get_leave_balance_id.save()


# monthly query
@login_required(login_url='home')
def monthly_query(request):
    if "sel_month" and "sel_year" in request.POST:
        selected_month = request.POST["sel_month"]
        selected_year = request.POST["sel_year"]
        if selected_month == selected_month and selected_year == selected_year:
            query_monthly = month_and_year.objects.filter(Month=selected_month, Year=selected_year)
            return render(request, 'monthly_query.html', locals())


# Total monthly leave taken group by staff name
@login_required(login_url='home')
def monthly_leave_taken(request):
    users = User.objects.annotate(new_leave_tot_w_days=Sum('newleave__Total_working_days'))
    return render(request, "result.html", locals())


@login_required(login_url='home')
def select_an_option(request):
    if "sel_an_option" in request.POST:
        selected_annual = request.POST["sel_an_option"]
        if selected_annual == 'Annual':
            return HttpResponseRedirect('/allStaffLeaves')
        elif selected_annual == 'Sick':
            return HttpResponseRedirect('/display_sick_leave')


@login_required(login_url='home')
def select_leave_and_department(request):
    if "sel_leave_option" and "sel_department" in request.POST:
        selected_leave = request.POST["sel_leave_option"]
        selected_department = request.POST["sel_department"]
        if selected_leave == "Annual" and selected_department == selected_department:
            query_annual = NewLeave.objects.filter(department=selected_department)
            return render(request, 'display_annual_leave_by_department.html', {'query_annual': query_annual})

        elif selected_leave == "Sick" and selected_department == selected_department:
            query_sick = SickLeave.objects.filter(department=selected_department)
            return render(request, 'display_sick_leave_by_department.html', {'query_sick': query_sick})


@login_required(login_url='home')
def Sick_leave_report(request):
    sick_leave_rpt = SickLeave.objects.all()
    return render(request, 'sick_leave_rpt.html', {'sick_leave_rpt': sick_leave_rpt})


@login_required(login_url='home')
def Annual_leave_report(request):
    annual_leave_rpt = NewLeave.objects.all()
    return render(request, 'annual_leave_rpt.html', {'annual_leave_rpt': annual_leave_rpt})


# export files to csv file
@login_required(login_url='home')
def download_sick_leaves(request):
    csv_export = SickLeave.objects.values('user__first_name', 'user__last_name', 'Leave_type', 'department',
                                          'Date_illness_began', 'Date_illness_end',
                                          'Total_working_days', 'Brief_explanation_of_illness',
                                          'Manager_Authorization_Status',
                                          'Authorized_by_Manager', 'Director_Authorization_Status',
                                          'Authorized_by_Director')
    return render_to_csv_response(csv_export)


@login_required(login_url='home')
def download_annual_leaves(request):
    csv_export = NewLeave.objects.values('user__first_name', 'user__last_name', 'Leave_type', 'department',
                                         'Start_Date', 'End_Date',
                                         'Total_working_days', 'Reason',
                                         'Manager_Authorization_Status',
                                         'Authorized_by_Manager', 'Director_Authorization_Status',
                                         'Authorized_by_Director')
    return render_to_csv_response(csv_export)


@login_required(login_url='home')
def display_sick_leave_by_id(request, staff_id):
    display_sick = SickLeave.objects.filter(id=staff_id)
    return render(request, 'display_sick_leave_report.html', {'display_sick': display_sick})


@login_required(login_url='home')
def display_annual_leave_by_id(request, staff_id):
    display_annual = NewLeave.objects.filter(id=staff_id)
    return render(request, 'display_annual_leave_report.html', {'display_annual': display_annual})
