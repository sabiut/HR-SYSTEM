from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render

from medical_scheme.forms import medical_form, User_form, FC_process_Form
from medical_scheme.models import medical_details, medical_entitlement


@login_required(login_url='home')
def medical_scheme_form(request):
    if request.POST:
        user_form = User_form(request.POST, instance=request.user)
        medical_details_form = medical_form(request.POST, request.FILES)
        if user_form.is_valid() and medical_details_form.is_valid():
            user = user_form.save()
            new_leave = medical_details_form.save(commit=False)
            new_leave.user = user
            new_leave.save()
            send_medical_email_to_FC(request)

            return render(request, "medical_detail_thank_you.html")
    else:
        user_form = User_form(instance=request.user)
        medical_details_form = medical_form()
    return render(request, 'medical_form.html', locals())


@login_required(login_url='home')
def send_medical_email_to_FC(request):
    email_obj = medical_details.objects.order_by('-pk')[0]
    if request.user.is_authenticated:
        in_group = User.objects.filter(groups__name="authorizer").filter(groups__name="Finance")
        for a in in_group:
            to_emails = a.email
            send_mail("Medical Scheme",
                      email_obj.user.first_name + " " + email_obj.user.last_name + " " + "have submitted his medical "
                                                                                         " details " + " "

                                                                                                       "Please "
                                                                                                       "login to "
                                                                                                       " http://127.0.0.1:8000/ to "
                                                                                                       " Update the "
                                                                                                       " applican's "
                                                                                                       " Medical Entitlement. "
                                                                                                       "\nMedical Detail "
                                                                                                       "Summary:"
                                                                                                       "\n" + "Type of medical checkup: " +
                      email_obj.medical_check_type + "\n" +
                      "Total cost: " + "{:,.2f}".format(email_obj.Total_Cost) + "$",
                      "Medical Scheme <eleavesystem@vfsc.vu>",
                      [to_emails])


@login_required(login_url='home')
def all_medical_details(request):
    all_medical = medical_details.objects.filter(Status='Review')
    return render(request, 'all_medical_details.html', locals())


@login_required(login_url='home')
def processed_medical_details(request):
    all_medical = medical_details.objects.filter(Status='Processed')
    return render(request, 'approved_medical_details.html', locals())


@login_required(login_url='home')
def processed_medical_details_profile(request):
    get_user_id = request.user.id
    all_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed')
    return render(request, 'approved_medical_details_profile.html', locals())


@login_required(login_url='home')
def processed_medical_details_authorizer(request):
    get_user_id = request.user.id
    all_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed')
    return render(request, 'approved_medical_details_authorizer.html', locals())


@login_required(login_url='home')
def processed_medical_details_director(request):
    get_user_id = request.user.id
    all_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed')
    return render(request, 'approved_medical_details_director.html', locals())


@login_required(login_url='home')
def processed_medical_details_hr(request):
    get_user_id = request.user.id
    all_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed')
    return render(request, 'approved_medical_details_hr.html', locals())


@login_required(login_url='home')
def Financial_controller_process_medical_details(request, staffs_id):
    if request.method == 'POST':
        get_staff_id = medical_details.objects.get(id=staffs_id)
        name = get_staff_id.user
        form = FC_process_Form(request.POST, instance=get_staff_id)
        if form.is_valid():
            calculate_medical_Balance(get_staff_id)
            form.save()
            FC_send_medical_email_to_staff(get_staff_id)
            return render(request, 'process_success.html', {'name': name})

    else:
        get_staff_id = medical_details.objects.get(id=staffs_id)
        form = FC_process_Form(instance=get_staff_id)

    return render(request, 'fc_processing_form.html', {'form': form})


@login_required(login_url='home')
def FC_send_medical_email_to_staff(staff_id):
    to_emails = staff_id.user.email
    if staff_id.Status == 'Processed':
        send_mail("Processed Medical Scheme",
                  "We have good news for you, the Financial Controller have successfully processed your Medial "
                  "details. Your medical entitlement has been automatically updated. " + " ",
                  "Processed Medical Scheme" "<eleavesystem@vfsc.vu>",

                  [to_emails], fail_silently=False)


def calculate_medical_Balance(staff_id):
    update_balance = staff_id
    set_user = update_balance.user
    get_user = medical_entitlement.objects.get(user=set_user)
    get_user.annual_entitlement = get_user.annual_entitlement - update_balance.Total_Cost
    get_user.save()
