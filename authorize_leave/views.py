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
