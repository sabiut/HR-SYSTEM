from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User, Group

# Create your views here.
from djqscsv import render_to_csv_response

from login.models import Leave_Balance, Sick_leave_balance, Sick_leave_month_year, Profile
from staff_balance.forms import update_leave_balance_form


@login_required(login_url='home')
def staff_balance(request):
    balance = Leave_Balance.objects.all()
    return render(request, 'display_staff_balance.html', {'balance': balance})


@login_required(login_url='home')
def staff_balances_director(request):
    balance = Leave_Balance.objects.all()
    return render(request, 'display_staff_balance_director.html', {'balance': balance})


@login_required(login_url='home')
def update_staff_balance_form(request, staffs_id):
    if request.method == 'POST':
        get_staff_id = Leave_Balance.objects.get(user_id=staffs_id)
        name = get_staff_id.user
        form = update_leave_balance_form(request.POST, instance=get_staff_id)
        if form.is_valid():
            # calculateBalance(get_staff_id)
            form.save()
            # director_send_email_to_staff(request, get_staff_id)
            return render(request, 'update_balance_success.html', {'name': name})

    else:
        get_staff_id = Leave_Balance.objects.get(user_id=staffs_id)
        form = update_leave_balance_form(instance=get_staff_id)

    return render(request, 'update_leave_balance_form.html', {'form': form})


@login_required(login_url='home')
def staff_sick_leave_balances(request):
    staff_sick_balance = Sick_leave_balance.objects.all()
    return render(request, 'display_sick_leave_balance.html', {'staff_sick_balance': staff_sick_balance})


# get staff annual balance by department name
@login_required(login_url='home')
def staff_balances_authorizer(request):
    query_set = Group.objects.filter(user=request.user)
    balance = Profile.objects.filter(department=query_set[1])
    return render(request, 'display_staff_balance_authorizer_page.html', {'balance': balance})


# get staff balance by department name
@login_required(login_url='home')
def staff_sick_leave_balances_authorizer(request):
    query_set = Group.objects.filter(user=request.user)
    balance = Profile.objects.filter(department=query_set[1])
    return render(request, 'display_sick_leave_balance_authorizer_page.html', {'balance': balance})


def download_staff_balance(request):
    csv_export = Leave_Balance.objects.values('user__first_name', 'user__last_name',
                                              'user__monthly_entitlement__entitlement', 'Leave_current_balance'
                                              )
    return render_to_csv_response(csv_export)


def download_staff_sick_balance(request):
    csv_export = Sick_leave_balance.objects.values('user__first_name', 'user__last_name', 'sick_leave_balance'
                                                   )
    return render_to_csv_response(csv_export)
