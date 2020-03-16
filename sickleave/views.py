from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render

from sickleave.forms import sick_leave_form
from leaveform.forms import User_form

from login.models import SickLeave


@login_required(login_url='home')
def sick_leave_application(request):
    if request.POST:
        user_form = User_form(request.POST, instance=request.user)
        sick_application_form = sick_leave_form(request.POST, request.FILES)

        if user_form.is_valid() and sick_application_form.is_valid():
            user = user_form.save()
            sick_form = sick_application_form.save(commit=False)
            sick_form.user = user
            sick_form.save()
            send_email_to_sick_leave_Authorizer(request)  # call email method
            return render(request, 'success_launch_sick_leave.html')
    else:
        user_form = User_form(instance=request.user)
        sick_application_form = sick_leave_form()

    return render(request, 'sick_leave_applications.html', locals())


@login_required(login_url='home')
def send_email_to_sick_leave_Authorizer(request):
    email_obj = SickLeave.objects.order_by('-pk')[0]
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
                send_mail("Director Sick Leave Application Form",
                          email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for a Sick "
                                                                                             "leave. "
                                                                                             "Please "
                                                                                             "login to "
                                                                                             "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                             "Authorize the leave.",
                          "Sick Leave Application <eleavesystem@rbv.gov.vu>",
                          [to_emails])
        elif request.user.groups.filter(name="authorizer").exists():
            for a in in_director:
                to_emails = a.email
                send_mail("Manager Sick Leave Application",
                          email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for a Sick "
                                                                                             "leave. "
                                                                                             "Please "
                                                                                             "login to "
                                                                                             "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                             "Authorize the leave.",
                          "Manager Sick Leave Application <eleavesystem@rbv.gov.vu>",
                          [to_emails])

        else:
            for a in in_group:
                to_emails = a.email
                send_mail("Sick Leave Application Form",
                          email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for an Sick "
                                                                                             "leave. "
                                                                                             "Please "
                                                                                             "login to "
                                                                                             "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                             "Authorize the leave.",
                          "Sick Leave Application <eleavesystem@rbv.gov.vu>",
                          [to_emails])


@login_required(login_url='home')
def display_sick_leave_Authorizer_page(request):
    query_set = Group.objects.filter(user=request.user)
    sick_leaves = SickLeave.objects.filter(department=query_set[1], Manager_Authorization_Status="Pending").filter(
        ~Q(user__groups__name='authorizer'))
    return render(request, 'display_sick_leave_hr_page.html', {'sick_leaves': sick_leaves})


@login_required(login_url='home')
def sick_leave_pending_director_approval(request):
    query_set = Group.objects.filter(user=request.user)
    sick_leaves = SickLeave.objects.filter(department=query_set[1],
                                           Manager_Authorization_Status="Approved",
                                           Director_Authorization_Status='Pending')
    return render(request, 'display_sick_pending_director_authorizer_page.html', {'sick_leaves': sick_leaves})
