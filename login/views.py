from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import admin, auth
from django.contrib.auth.models import User, Group
import socket

# Home page
from .models import NewLeave, SickLeave, encashment


def home(request):
    return render(request, "home.html")


def invalid_page(request):
    return render(request, 'home.html')


# Authenticate user
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        to_emails = user.email
        ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ip:
            ip = ip.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDRESS", " ")
            get_ip = socket.gethostbyname(socket.gethostname())
            send_mail("RBV eLeave", "Your eleave Profile have been access from the IP:" +
                      get_ip + ". " + " Please report this to the administrator if you find this suspicious",
                      "eleave security info <eleavesystem@vfsc.vu>", [to_emails])

            if user.groups.filter(name="Director").exists():
                return HttpResponseRedirect('/director_page')

            elif user.groups.filter(name="HR").exists():
                return HttpResponseRedirect('/hr')
            elif user.groups.filter(name="authorizer").exists():
                return HttpResponseRedirect('/authorizer_page')
            else:
                return HttpResponseRedirect('/profile_page')
    else:
        return HttpResponseRedirect('/invalid_page')


# Filter annual leaves by login user
@login_required(login_url='home')
def display_pending_annual_leave(request):
    if request.user.is_authenticated:
        get_user_id = request.user.id
        display = NewLeave.objects.filter(user_id=get_user_id, Manager_Authorization_Status="Pending")
        return render(request, 'display_login_user_annual_leave.html', {'display': display})


@login_required(login_url='home')
def director_page(request):
    username = None
    if request.user.is_authenticated:
        try:
            profile_info = request.user.leave_balance
            entitlements = request.user.monthly_entitlement
            # sick_leave_balance = request.user.sick_leave_balance
            # medical_entitlement = request.user.medical_entitlement
            info = request.user
            query_set = Group.objects.filter(user=request.user)
            get_user_id = request.user.id
            pending_leave_count = NewLeave.objects.filter(department=query_set[1],
                                                          Manager_Authorization_Status="Pending").count()
            approved_leave_count = NewLeave.objects.filter(department=query_set[2],
                                                           Manager_Authorization_Status="Approved",
                                                           Director_Authorization_Status='Pending', Archived='').count()
            allapprovedleaves = NewLeave.objects.filter(department=query_set[2],
                                                        Manager_Authorization_Status="Approved",
                                                        Director_Authorization_Status='Approved', Archived='').count()

            # count sick leaves
            count_sick_leaves = SickLeave.objects.filter(department=query_set[1],
                                                         Manager_Authorization_Status="Pending").count()

            count_approved_sick_leave = SickLeave.objects.filter(department=query_set[2],
                                                                 Manager_Authorization_Status="Approved",
                                                                 Director_Authorization_Status='Pending',
                                                                 Archived='').count()

            count_all_approved_sick_leaves = SickLeave.objects.filter(department=query_set[2],
                                                                      Manager_Authorization_Status="Approved",
                                                                      Director_Authorization_Status='Approved',
                                                                      Archived='').count()

            count_manager_annual_leave = NewLeave.objects.filter(department=query_set[2],
                                                                 user__groups__name='authorizer').filter(
                Director_Authorization_Status='Pending').count()
            count_manager_approved_annual_leave = NewLeave.objects.filter(department=query_set[2],
                                                                          user__groups__name='authorizer'). \
                filter(Director_Authorization_Status='Approved').count()
            count_manager_sick_leaves = SickLeave.objects.filter(department=query_set[2],
                                                                 user__groups__name='authorizer'). \
                filter(Director_Authorization_Status='Pending').count()
            count_manager_approved_sick_leave = SickLeave.objects.filter(department=query_set[2],
                                                                         user__groups__name='authorizer'). \
                filter(Director_Authorization_Status='Approved').count()

            count_pending_encashment = encashment.objects.filter(approval_status='Pending').count()
            count_approved_encashments = encashment.objects.filter(approval_status='Approved').count()
            # count_staff_loan = staff_loan.objects.filter(review_status="Reviewed", approval_status='Pending').count()
            # count_approved_loans = staff_loan.objects.filter(review_status='Reviewed',
            #                                                  approval_status='Approved').count()
            #
            # count_reviewed_house_loans = Loan_details.objects.filter(Housing_loan_committee_Recommended_for='Approval',
            #                                                          Approval_status='Pending').count()
            #
            # count_approve_house_loans = Loan_details.objects.filter(Housing_loan_committee_Recommended_for='Approval',
            #                                                         Approval_status='Approved').count()
            # count_processed_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed').count()

            count_director_pending_annual_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                                          user__groups__name='Director').filter(
                Director_Authorization_Status='Pending').count()

            count_director_approved_annual_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                                           user__groups__name='Director').filter(
                Director_Authorization_Status='Approved').count()

            count_director_pending_sick = SickLeave.objects.filter(user_id=get_user_id,
                                                                   user__groups__name='Director').filter(
                Director_Authorization_Status='Pending').count()
            count_director_approved_sick = SickLeave.objects.filter(user_id=get_user_id,
                                                                    user__groups__name='Director').filter(
                Director_Authorization_Status='Approved').count()

            return render(request, 'director_page.html', locals())
        except ObjectDoesNotExist:
            return render(request, 'throw_balance_error.html')


@login_required(login_url='home')
def profile_page(request):
    username = None
    if request.user.is_authenticated:
        try:
            profile_info = request.user.leave_balance
            entitlements = request.user.monthly_entitlement
            # sick_leave_balance = request.user.sick_leave_balance
            # medical_entitlement = request.user.medical_entitlement
            info = request.user
            query_set = Group.objects.filter(user=request.user)
            get_user_id = request.user.id
            count_pending_leave_profile = NewLeave.objects.filter(user_id=get_user_id,
                                                                  Manager_Authorization_Status="Pending").count()
            count_manager_approved_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                                   Manager_Authorization_Status="Approved",
                                                                   Director_Authorization_Status='Pending',
                                                                   Archived='').count()
            count_all_approved_annual_leaves = NewLeave.objects.filter(user_id=get_user_id,
                                                                       Manager_Authorization_Status="Approved",
                                                                       Director_Authorization_Status='Approved',
                                                                       Archived='').count()

            count_pending_sick_leave_profile = SickLeave.objects.filter(user_id=get_user_id,
                                                                        Manager_Authorization_Status="Pending").count()

            count_manager_approved_sick_leave = SickLeave.objects.filter(user_id=get_user_id,
                                                                         Manager_Authorization_Status="Approved",
                                                                         Director_Authorization_Status='Pending',
                                                                         Archived='').count()

            count_all_Director_approved_sick_leaves = SickLeave.objects.filter(user_id=get_user_id,
                                                                               Manager_Authorization_Status="Approved",
                                                                               Director_Authorization_Status='Approved',
                                                                               Archived='').count()
            count_pending_encashment = encashment.objects.filter(approval_status='Pending').count()

            count_pending_encashment_profile = encashment.objects.filter(user_id=get_user_id,
                                                                         approval_status='Pending').count()
            count_approved_encashment_profile = encashment.objects.filter(user_id=get_user_id,
                                                                          approval_status='Approved').count()
            # count_loan_pending_loans = staff_loan.objects.filter(user_id=get_user_id, review_status="Pending").count()
            # count_review_staff_loans = staff_loan.objects.filter(user_id=get_user_id, review_status="Reviewed",
            #                                                      approval_status='Pending').count()
            # count_approved_staff_loans = staff_loan.objects.filter(user_id=get_user_id, review_status="Reviewed",
            #                                                        approval_status='Approved').count()
            #
            # count_house_loan_to_be_review = Loan_details.objects.filter(user_id=get_user_id,
            #                                                             Housing_loan_committee_Recommended_for='Review').count()
            # count_reviewed_house_loan = Loan_details.objects.filter(user_id=get_user_id,
            #                                                         Housing_loan_committee_Recommended_for='Approval',
            #                                                         Approval_status='Pending').count()
            #
            # count_approved_house_loans = Loan_details.objects.filter(user_id=get_user_id,
            #                                                          Housing_loan_committee_Recommended_for='Approval',
            #                                                          Approval_status='Approved').count()
            # count_processed_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed').count()

            return render(request, "profile_page.html", locals())
        except ObjectDoesNotExist:
            return render(request, 'throw_balance_error.html')


# authorises home page@login_required(login_url='home')
@login_required(login_url='home')
def authorizer_page(request):
    username = None
    if request.user.is_authenticated:
        try:
            profile_info = request.user.leave_balance
            entitlements = request.user.monthly_entitlement
            # sick_leave_balance = request.user.sick_leave_balance
            # medical_entitlement = request.user.medical_entitlement
            info = request.user
            query_set = Group.objects.filter(user=request.user)
            get_user_id = request.user.id

            count_manager_annual_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                                 user__groups__name='authorizer').filter(
                Director_Authorization_Status='Pending').count()
            count_manager_approved_annual_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                                          user__groups__name='authorizer'). \
                filter(Director_Authorization_Status='Approved').count()

            count_pending_sick_leave_profile = SickLeave.objects.filter(user_id=get_user_id,
                                                                        Manager_Authorization_Status="Pending").count()

            count_manager_approved_sick_leave = SickLeave.objects.filter(user_id=get_user_id,
                                                                         Manager_Authorization_Status="Approved",
                                                                         Director_Authorization_Status='Pending',
                                                                         Archived='').count()

            count_all_Director_approved_sick_leaves = SickLeave.objects.filter(user_id=get_user_id,
                                                                               Manager_Authorization_Status="Approved",
                                                                               Director_Authorization_Status='Approved',
                                                                               Archived='').count()
            # count only pending leaves that are belong to staffs not the authorizer(managers)
            pending_leave_count = NewLeave.objects.filter(department=query_set[1],
                                                          Manager_Authorization_Status="Pending").filter(
                ~Q(user__groups__name='authorizer')).count()
            approved_leave_count = NewLeave.objects.filter(department=query_set[1],
                                                           Manager_Authorization_Status="Approved",
                                                           Director_Authorization_Status='Pending', Archived='').count()
            allapprovedleaves = NewLeave.objects.filter(department=query_set[1],
                                                        Manager_Authorization_Status="Approved",
                                                        Director_Authorization_Status='Approved', Archived='').count()

            # count sick leaves
            count_sick_leaves = SickLeave.objects.filter(department=query_set[1],
                                                         Manager_Authorization_Status="Pending").filter(
                ~Q(user__groups__name='authorizer')).count()

            count_approved_sick_leave = SickLeave.objects.filter(department=query_set[1],
                                                                 Manager_Authorization_Status="Approved",
                                                                 Director_Authorization_Status='Pending',
                                                                 Archived='').count()

            count_all_approved_sick_leaves = SickLeave.objects.filter(department=query_set[1],
                                                                      Manager_Authorization_Status="Approved",
                                                                      Director_Authorization_Status='Approved',
                                                                      Archived='').count()

            count_pending_encashment_profile = encashment.objects.filter(user_id=get_user_id,
                                                                         approval_status='Pending').count()
            count_approved_encashment_profile = encashment.objects.filter(user_id=get_user_id,
                                                                          approval_status='Approved').count()

            # count_processed_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed').count()

            count_authorier_pending_sick = SickLeave.objects.filter(user_id=get_user_id,
                                                                    user__groups__name='authorizer').filter(
                Director_Authorization_Status='Pending').count()

            count_authorizer_approved_sick = SickLeave.objects.filter(user_id=get_user_id,
                                                                      user__groups__name='authorizer').filter(
                Director_Authorization_Status='Approved').count()

            return render(request, 'authorizer_page.html', locals())
        except ObjectDoesNotExist:
            return render(request, 'throw_balance_error.html')


# log user out
def log_out(request):
    auth.logout(request)
    return render(request, 'home.html')


@login_required(login_url='home')
def hr(request):
    username = None
    if request.user.is_authenticated:
        try:
            profile_info = request.user.leave_balance
            entitlements = request.user.monthly_entitlement
            # medical_entitlement = request.user.medical_entitlement
            info = request.user
            # sick_leave_balance = request.user.sick_leave_balance
            get_user_id = request.user.id
            approved_leaves = NewLeave.objects.filter(Manager_Authorization_Status='Approved',
                                                      Director_Authorization_Status='Approved').count()
            rejected_leaves = NewLeave.objects.filter(Manager_Authorization_Status='Rejected',

                                                      Director_Authorization_Status='Rejected').count()

            count_pending_encashment_profile = encashment.objects.filter(user_id=get_user_id,
                                                                         approval_status='Pending').count()
            count_approved_encashment_profile = encashment.objects.filter(user_id=get_user_id,
                                                                          approval_status='Approved').count()

            # count_processed_medical = medical_details.objects.filter(user_id=get_user_id, Status='Processed').count()

            count_hr_pending_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                             Manager_Authorization_Status="Pending").count()
            count_hr_approved_leave = NewLeave.objects.filter(user_id=get_user_id,
                                                              Manager_Authorization_Status="Approved",
                                                              Director_Authorization_Status='Pending',
                                                              Archived='').count()
            count_hr_director_approved_leaves = NewLeave.objects.filter(user_id=get_user_id,
                                                                        Manager_Authorization_Status="Approved",
                                                                        Director_Authorization_Status='Approved',
                                                                        Archived='').count()
            count_pending_sick_leave = SickLeave.objects.filter(user_id=get_user_id,
                                                                Manager_Authorization_Status="Pending").count()

            count_manager_approved_sick_leave = SickLeave.objects.filter(user_id=get_user_id,
                                                                         Manager_Authorization_Status="Approved",
                                                                         Director_Authorization_Status='Pending',
                                                                         Archived='').count()
            count_sick_approved_by_director = SickLeave.objects.filter(user_id=get_user_id,
                                                                       Manager_Authorization_Status="Approved",
                                                                       Director_Authorization_Status='Approved',
                                                                       Archived='').count()

            return render(request, "hr_page.html", locals())
        except ObjectDoesNotExist:
            return render(request, 'throw_balance_error.html')


# get site header for password change form text
class CustomResetPasswordView(PasswordResetView):
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['site_header'] = getattr(admin.sites.AdminSite,
                                         'site_header')  # get site header text. For django 2.X it should be getattr(admin.sites.AdminSite, 'site_header')
        return context
