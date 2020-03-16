from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import csrf

from encashment.forms import User_form, leave_encashment_form, director_authorize_encashment_form, \
    processing_encashment_form
from login.models import encashment, Leave_Balance
#from medical_scheme.models import medical_details


@login_required(login_url='home')
def encashment_application(request):
    if request.POST:
        user_form = User_form(request.POST, instance=request.user)
        encashment_form = leave_encashment_form(request.POST)

        if user_form.is_valid() and encashment_form.is_valid():
            user = user_form.save()
            new_leave = encashment_form.save(commit=False)
            new_leave.user = user
            new_leave.save()
            send_encashment_email_to_Director(request)  # call the email method to send email to authorizer
            return render(request, "encashment_application_thanks.html")
    else:
        user_form = User_form(instance=request.user)
        encashment_form = leave_encashment_form()
    args = {}
    args.update(csrf(request))
    args['user_form'] = user_form
    args['encashment_form'] = encashment_form
    return render(request, 'encashment_application_form.html', args)


@login_required(login_url='home')
def send_encashment_email_to_Director(request):
    email_obj = encashment.objects.order_by('-pk')[0]
    if request.user.is_authenticated:
        query_set = Group.objects.filter(user=request.user)
        in_group = User.objects.filter(groups__name=query_set[0]).filter(groups__name="Director")
        for a in in_group:
            to_emails = a.email
            send_mail("Leave Encashment Application Form",
                      email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have apply for an Annual "
                                                                                         "Leave "
                                                                                         "Encashment. "
                                                                                         "Please "
                                                                                         "login to "
                                                                                         "http://ec2-18-212-65-46.compute-1.amazonaws.com/ to "
                                                                                         "Authorize the leave "
                                                                                         "encashment.",
                      "Annual Leave Encashment  <eleavesystem@rbv.gov.vu>",
                      [to_emails])
