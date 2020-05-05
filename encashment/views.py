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


# from medical_scheme.models import medical_details
from medical_scheme.models import medical_details


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
                                                                                         "http://127.0.0.1:8000/ to "
                                                                                         "Authorize the leave "
                                                                                         "encashment.",
                      "Annual Leave Encashment  <eleavesystem@rbv.gov.vu>",
                      [to_emails])


@login_required(login_url='home')
def pending_encashments_athorizer(request):
    pending_encashments = encashment.objects.filter(approval_status='Pending')
    return render(request, 'my_pending_encashments_auth.html', {'pending_encashments': pending_encashments})


@login_required(login_url='home')
def pending_encashments_director(request):
    pending_encashments = encashment.objects.filter(approval_status='Pending')
    return render(request, 'pending_encashments.html', {'pending_encashments': pending_encashments})


@login_required(login_url='home')
def approved_encashments_authorizer(request):
    pending_encashments = encashment.objects.filter(approval_status='Approved')
    return render(request, 'approved_encashments.html', {'pending_encashments': pending_encashments})


@login_required(login_url='home')
def pending_encashments_profile(request):
    get_user_id = request.user.id
    pending_encashments = encashment.objects.filter(user_id=get_user_id, approval_status='Pending')
    return render(request, 'pending_encashments_profile.html', {'pending_encashments': pending_encashments})


@login_required(login_url='home')
def approved_encashments_profile(request):
    if request.user.is_authenticated:
        get_user_id = request.user.id
        pending_encashments = encashment.objects.filter(user_id=get_user_id, approval_status='Approved')
        return render(request, 'approved_encashments_profile.html', {'pending_encashments': pending_encashments})


@login_required(login_url='home')
def director_authorize_encashment(request, staff_id):
    if request.method == 'POST':
        get_id = encashment.objects.get(id=staff_id)
        form = director_authorize_encashment_form(request.POST, instance=get_id)
        name = get_id.user
        if form.is_valid():
            director_send_encashment_email_to_staff(request, get_id)
            send_email_to_Financial_Controller(request, get_id)

            form.save()
            return render(request, 'commissioner_success.html', {'name': name})

    else:
        get_id = encashment.objects.get(id=staff_id)
        form = director_authorize_encashment_form(instance=get_id)
    return render(request, 'commissioner_auth_encashment_form.html', {'form': form})


def director_send_encashment_email_to_staff(request, staff_id):
    to_emails = staff_id.user.email
    if staff_id.approval_status == 'Approved':
        send_mail("leave Encashment approved by Director" + " " + staff_id.Authorize_by,
                  "We have good news for you, the Director Mr" + " " + staff_id.Authorize_by + " " + "have " + staff_id.approval_status
                  + " " + " your leave encashment and" + " " +
                  "We have forwarded the encashment application to the Financial Controller to process the payment.",
                  "Leave encashment" "<eleavesystem@rbv.gov.vu>",
                  [to_emails])
    elif staff_id.approval_status == 'Rejected':
        send_mail("Leave encashment Application Rejected by" + " " + staff_id.Authorize_by,
                  "We have bad news for you, Your leave encashment have been {}".format(
                      staff_id.approval_status) + " " + "by the Director {}".format(
                      staff_id.Authorize_by) + ". " + "\n Consult the Director for more"
                                                      "information."
                  ,
                  "Leave encashment <eLeavesystem@rbv.gov.vu>", [to_emails], fail_silently=False)


@login_required(login_url='home')
def send_email_to_Financial_Controller(request, staff_id):
    query_set = Group.objects.filter(user=request.user)
    in_group = User.objects.filter(groups__name="authorizer").filter(groups__name="Finance")
    for a in in_group:
        to_send = [a.email]
        if staff_id.approval_status == 'Approved':
            send_mail("Leave encashment",
                      "The Director Mr " + " " + staff_id.Authorize_by + " " + "have " + staff_id.approval_status
                      + " " + staff_id.user.first_name + "'s" + " " + "leave encashment and we have forwarded it to you "
                                                                      "to process the payment "
                                                                      "\n" +
                      "Please login to http://127.0.0.1:8000/.",
                      "Leave encashment " "<eleavesystem@vfsc.vu>",
                      to_send)


@login_required(login_url='home')
def financial_controller(request):
    in_group = User.objects.filter(groups__name="authorizer").filter(groups__name="Finance")
    if request.user.is_authenticated:
        if request.user in in_group:
            all_approved_encashments = encashment.objects.filter(approval_status="Approved",
                                                                 processing="Processing").count()
            all_process = encashment.objects.filter(approval_status="Approved", processing='Completed').count()
            count_medical_details = medical_details.objects.filter(Status='Review').count()
            count_process_medicals = medical_details.objects.filter(Status='Processed').count()
            c = {'all_approved_encashments': all_approved_encashments,
                 'all_process': all_process,
                 'count_medical_details': count_medical_details,
                 'count_process_medicals': count_process_medicals
                 }
            return render(request, 'financial_controller.html', c)
        else:
            return render(request, 'no_access.html')


@login_required(login_url='home')
def all_encashments(request):
    all_encashments = encashment.objects.filter(approval_status="Approved", processing="Processing")
    return render(request, 'encashments_pending_payment.html', {'all_encashments': all_encashments})


@login_required(login_url='home')
def all_processed_encashments(request):
    all_processed_encashments = encashment.objects.filter(approval_status="Approved", processing='Completed')
    return render(request, 'all_process_encasments.html', {'all_processed_encashments': all_processed_encashments})


@login_required(login_url='home')
def financial_controller_processed_pay(request, staff_id):
    if request.method == 'POST':
        get_id = encashment.objects.get(id=staff_id)
        form = processing_encashment_form(request.POST, instance=get_id)
        name = get_id.user
        if form.is_valid():
            calculate_updated_leave_Balance(get_id)
            FC_send_encashment_email_to_staff(request, get_id)
            form.save()
            return render(request, 'financial_controller_success.html', {'name': name})

    else:
        get_id = encashment.objects.get(id=staff_id)
        form = processing_encashment_form(instance=get_id)
    return render(request, 'process_encashmentForm.html', {'form': form})


@login_required(login_url='home')
def FC_send_encashment_email_to_staff(request, staff_id):
    to_emails = staff_id.user.email
    if staff_id.processing == 'Completed':
        send_mail("Encashment process completed",
                  "We have good news for you, the Financial Controller have successfully processed your leave "
                  "encashment. Your annual leave balance has been automatically updated. " + " " +
                  "Consult the financial controller to collect your Cheque.",
                  "Encashment process completed" "<eleavesystem@rbv.gov.vu>",
                  [to_emails], fail_silently=False)


@login_required(login_url='home')
def calculate_updated_leave_Balance(staff_id):
    update_balance = staff_id
    set_user = update_balance.user
    get_user = Leave_Balance.objects.get(user=set_user)
    get_user.Leave_current_balance = get_user.Leave_current_balance - update_balance.total_number_of_days
    get_user.save()


@login_required(login_url='home')
def encashment_report(request, staff_id):
    report = encashment.objects.filter(id=staff_id)
    return render(request, 'encashment_report.html', {'report': report})
