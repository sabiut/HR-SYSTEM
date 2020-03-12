from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import Group
# Create your views here.
from django.template.context_processors import csrf

from .forms import *
from login.models import Leave_Balance


@login_required(login_url='home')
def leave_application(request):
    if request.POST:
        user_form = User_form(request.POST, instance=request.user)
        leave_form = application_form(request.POST)
        if user_form.is_valid() and leave_form.is_valid():
            number_of_days = leave_form.cleaned_data['Total_working_days']
            get_user = Leave_Balance.objects.get(user_id=request.user.id)
            leave_balance = get_user.Leave_current_balance
            if number_of_days > leave_balance:
                return HttpResponseRedirect('/insufficient_balance')

            else:
                user = user_form.save()
                new_leave = leave_form.save(commit=False)
                new_leave.user = user
                new_leave.save()
                send_email_to_Authorizer(request)  # call the email method to send email to authorizer
                return render(request, "leave_application_thanks.html")
    else:
        user_form = User_form(instance=request.user)
        leave_form = application_form()
        args = {}
        args.update(csrf(request))
        args['user_form'] = user_form
        args['leave_form'] = leave_form
        return render(request, 'leave_application.html', args)


def insufficient_balance(request):
    return render(request, "error_insufficient_balance.html")


@login_required(login_url='home')
def leave_options(request):
    return render(request, 'leave_option.html')


def select_leave_type(request):
    if "sel_leave_option" in request.POST:
        selected_annual = request.POST["sel_leave_option"]
        if selected_annual == 'Annual':
            return HttpResponseRedirect('/leave_application')
        elif selected_annual == 'Sick':
            return HttpResponseRedirect('/sick_leave_application')
        elif selected_annual == 'Encashment':
            return HttpResponseRedirect('/encashment_application')
        elif selected_annual == 'Medical':
            return HttpResponseRedirect('/medical_scheme_form')


@login_required(login_url='home')
def send_email_to_Authorizer(request):
    email_obj = NewLeave.objects.order_by('-pk')[0]
    if request.user.is_authenticated:
        query_set = Group.objects.filter(user=request.user)
        in_group = User.objects.filter(groups__name=query_set[0]).filter(groups__name="authorizer")

        in_director = User.objects.filter(groups__name=query_set[0]).filter(groups__name="authorizer").filter(
            groups__name="Director").filter(groups__name=query_set[0])
        in_governor = User.objects.filter(groups__name=query_set[0]).filter(groups__name="authorizer").filter(
            groups__name="Governor")

        if request.user.groups.filter(name="Director").exists():
            for a in in_governor:
                to_emails = a.email
                send_mail("Director Leave Application Form",
                          email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for an annual "
                                                                                             "leave. "
                                                                                             "Please "
                                                                                             "login to "
                                                                                             "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                             "Authorize the leave.",
                          "Annual Leave Application <eleavesystem@rbv.gov.vu>",
                          [to_emails])
        elif request.user.groups.filter(name="authorizer").exists():
            for a in in_director:
                to_emails = a.email
                send_mail("Manager Leave Application Form",
                          email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for an annual "
                                                                                             "leave. "
                                                                                             "Please "
                                                                                             "login to "
                                                                                             "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                             "Authorize the leave.",
                          "Annual Leave Application <eleavesystem@rbv.gov.vu>",
                          [to_emails])

        else:
            for a in in_group:
                to_emails = a.email
                send_mail("Leave Application Form",
                          email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for an annual "
                                                                                             "leave. "
                                                                                             "Please "
                                                                                             "login to "
                                                                                             "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                             "Authorize the leave.",
                          "Annual Leave Application <eleavesystem@rbv.gov.vu>",
                          [to_emails])


@login_required(login_url='home')
def filter_manager_approved_annual_leave(request):
    query_set = Group.objects.filter(user=request.user)  # added that to filter by department
    in_group = NewLeave.objects.filter(department=query_set[2], user__groups__name='authorizer').filter(
        Director_Authorization_Status='Approved')
    return render(request, 'manager_approved_annual_leave_director.html', {'in_group': in_group})