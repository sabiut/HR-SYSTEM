from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.db.models import Q

from authorize_leave.forms import DirectorForm, ManagerForm, Manager_approve_sick_Form
from login.models import NewLeave, Leave_Balance, month_and_year, SickLeave, Sick_leave_balance


@login_required(login_url='home')
def Allleaves(request):
    query_set = Group.objects.filter(user=request.user)
    allleave = NewLeave.objects.filter(department=query_set[1], Manager_Authorization_Status="Pending").filter(
        ~Q(user__groups__name='authorizer'))
    return render(request, 'allleave.html', locals())


# Unit manager form to authorize leave
@login_required(login_url='home')
def UnitmanagerFrorm(request, staff_id):
    if request.method == 'POST':
        get_staff_id = NewLeave.objects.get(id=staff_id)
        form = ManagerForm(request.POST, instance=get_staff_id)
        if form.is_valid():
            name = get_staff_id.user
            manager_send_email_to_staff(request, get_staff_id)  # call send email to staff function
            send_email_to_Director(request, get_staff_id)  # call email function
            form.save()
            return render(request, 'Manage_success_authorize_page.html', {'name': name})

    else:
        get_staff_id = NewLeave.objects.get(id=staff_id)
        form = ManagerForm(instance=get_staff_id)
    return render(request, 'managerauthorisedform.html', {'form': form})


@login_required(login_url='home')
def manager_send_email_to_staff(request, staff_id):
    email_staff = staff_id.user.email
    if staff_id.Manager_Authorization_Status == 'Approved':
        send_mail("Leave Application Approved by" + " " + staff_id.Authorized_by_Manager,
                  "Your annual leave application have been {}".format(
                      staff_id.Manager_Authorization_Status) + " " + "by your Manager {}".format(
                      staff_id.Authorized_by_Manager) + " " + "and has now been forward to the "
                                                              "Director "
                                                              "for the final authorization.\nWe will "
                                                              "inform you via email once the Director "
                                                              "Authorized your Annual leave",
                  "Annual Leave <eLeavesystem@rbv.gov.vu>", [email_staff], fail_silently=False)
    elif staff_id.Manager_Authorization_Status == 'Rejected':
        send_mail("Leave Application Rejected by" + " " + staff_id.Authorized_by_Manager,
                  "We have bad news for you, Your annual leave application have been {}".format(
                      staff_id.Manager_Authorization_Status) + " " + "by your Manager {}".format(
                      staff_id.Authorized_by_Manager) + ". " + "\n We regret that we weren't able to"
                                                               "forward your leave to your unit director."
                                                               "\n Consult your unit manager for more information."
                  ,
                  "Annual Leave <eLeavesystem@rbv.gov.vu>", [email_staff], fail_silently=False)


@login_required(login_url='home')
def send_email_to_Director(request, staff_id):
    query_set = Group.objects.filter(user=request.user)
    in_group = User.objects.filter(groups__name="Director").filter(groups__name=query_set[1]).filter(
        groups__name="authorizer")
    for a in in_group:
        to_send = [a.email]

        send_mail("Approved annual Leave",
                  "The unit Manager" + " " + staff_id.Authorized_by_Manager + " " + "have " + staff_id.Manager_Authorization_Status
                  + " " + staff_id.user.first_name + "'s" + " " + "annual leave and we have forwarded it to you for "
                                                                  "final "
                                                                  "authorization\n" +
                  "Please login to http://ec2-18-212-65-46.compute-1.amazonaws.com/ to Authorize the leave.",
                  "Approved Annual Leave " "<eleavesystem@rbv.gov.vu>",
                  to_send)


@login_required(login_url='home')
def Tobeapprovebydirector(request):
    query_set = Group.objects.filter(user=request.user)
    all_manager_approved_leaves = NewLeave.objects.filter(department=query_set[2],
                                                          Manager_Authorization_Status="Approved",
                                                          Director_Authorization_Status='Pending')
    return render(request, 'tobe_approvebydirector.html', locals())


# Unit Director form to authorize leave
@login_required(login_url='home')
def unitDirectorForm(request, staffs_id):
    if request.method == 'POST':
        get_staff_id = NewLeave.objects.get(id=staffs_id)
        name = get_staff_id.user
        form = DirectorForm(request.POST, instance=get_staff_id)
        if form.is_valid():
            calculateBalance(get_staff_id)
            form.save()
            director_send_email_to_staff(request, get_staff_id)
            return render(request, 'director_success_approved_leave.html', {'name': name})

    else:
        get_staff_id = NewLeave.objects.get(id=staffs_id)
        form = DirectorForm(instance=get_staff_id)

    return render(request, 'director_authorize_form.html', {'form': form})


# update staff leave balance on director approval
def calculateBalance(staff_id):
    update_balance = staff_id
    set_user = update_balance.user
    get_user = Leave_Balance.objects.get(user=set_user)
    get_user.Leave_current_balance = get_user.Leave_current_balance - update_balance.Total_working_days
    get_user.save()


def director_send_email_to_staff(request, staff_id):
    to_emails = staff_id.user.email
    if staff_id.Director_Authorization_Status == 'Approved':
        send_mail("Annual Leave approved by" + " " + staff_id.Authorized_by_Director,
                  "We have good news for you, the unit Director" + " " + staff_id.Authorized_by_Director + " " + "have " + staff_id.Director_Authorization_Status
                  + " " + "your annual leave. \n" +
                  "Enjoy your holiday! :)",
                  "Annual Leave " "<eleavesystem@rbv.gov.vu>",
                  [to_emails])
    elif staff_id.Director_Authorization_Status == 'Rejected':
        send_mail("Leave Application Rejected by" + " " + staff_id.Authorized_by_Director,
                  "We have bad news for you, Your annual leave application have been {}".format(
                      staff_id.Director_Authorization_Status) + " " + "by your Director {}".format(
                      staff_id.Authorized_by_Director) + ". " + "\n Consult your unit Director for more"
                                                                "information."
                  ,
                  "Annual Leave <eLeavesystem@rbv.gov.vu>", [to_emails], fail_silently=False)


@login_required(login_url='home')
def approved_leaves(request):
    query_set = Group.objects.filter(user=request.user)
    approvedleaves = NewLeave.objects.filter(department=query_set[2], Manager_Authorization_Status="Approved",
                                             Director_Authorization_Status="Approved")
    return render(request, 'approvedleaves.html', locals())


@login_required(login_url='home')
def annual_pending_director_approval(request):
    query_set = Group.objects.filter(user=request.user)
    all_manager_approved_leaves = NewLeave.objects.filter(department=query_set[1],
                                                          Manager_Authorization_Status="Approved",
                                                          Director_Authorization_Status='Pending')
    return render(request, 'display_annual_pending_director_approval.html', locals())


@login_required(login_url='home')
def approved_leaves_authorizer_page(request):
    query_set = Group.objects.filter(user=request.user)
    approvedleaves = NewLeave.objects.filter(department=query_set[1], Manager_Authorization_Status="Approved",
                                             Director_Authorization_Status="Approved")
    return render(request, 'approvedleaves.html', locals())


# approve sick leave
@login_required(login_url='home')
def Unit_manager_approve_sick_Form(request, staff_id):
    if request.method == 'POST':
        get_staff_id = SickLeave.objects.get(id=staff_id)
        form = Manager_approve_sick_Form(request.POST, instance=get_staff_id)
        name = get_staff_id.user
        if form.is_valid():
            calculate_sick_leave_Balance(get_staff_id)
            form.save()
            manager_send_sick_leave_email_to_staff(request, get_staff_id)
            #Manager_send_sick_leave_email_to_Director(request, get_staff_id)
            return render(request, 'manager_success_authorize_sick.html', {'name': name})

    else:
        get_staff_id = SickLeave.objects.get(id=staff_id)
        form = Manager_approve_sick_Form(instance=get_staff_id)
    return render(request, 'manager_authorize_sick_form.html', {'form': form})


@login_required(login_url='home')
def manager_send_sick_leave_email_to_staff(request, staff_id):
    email_staff = staff_id.user.email
    if staff_id.Manager_Authorization_Status == 'Approved':
        send_mail("Sick Leave Application Approved by" + " " + staff_id.Authorized_by_Manager,
                  "We have good news for you. Your sick leave application have been {}".format(
                      staff_id.Manager_Authorization_Status) + " " + "by your Manager {}".format(
                      staff_id.Authorized_by_Manager) + " " + "We have updated your sick leave balance.\n Enjoy your "
                                                              " leave",
                  "Sick Leave <eLeavesystem@rbv.gov.vu>", [email_staff], fail_silently=False)
    elif staff_id.Manager_Authorization_Status == 'Rejected':
        send_mail("Sick Leave Application Rejected by" + " " + staff_id.Authorized_by_Manager,
                  "We have bad news for you, Your sick leave application have been {}".format(
                      staff_id.Manager_Authorization_Status) + " " + "by your Manager {}".format(
                      staff_id.Authorized_by_Manager) + ". " + "\n We regret that we weren't able to"
                                                               "forward your leave to your unit director."
                                                               "\n Consult your unit manager for more information."
                  ,
                  "Sick Leave <eLeavesystem@rbv.gov.vu>", [email_staff], fail_silently=False)


# update staff sick leave balance on director approval
def calculate_sick_leave_Balance(staff_id):
    update_balance = staff_id
    set_user = update_balance.user
    get_user = Sick_leave_balance.objects.get(user=set_user)
    get_user.sick_leave_balance = get_user.sick_leave_balance - update_balance.Total_working_days
    get_user.save()
