from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import add_holiday_form
from .models import *


# Create your views here.

@login_required(login_url='home')
def holidays(request):
    holidays = holiday.objects.all()
    return render(request, 'holiday.html', {'holidays': holidays})


@login_required(login_url='home')
def view_holidays_hr(request):
    holidays = holiday.objects.all()
    return render(request, 'view_holidays_hr.html', {'holidays': holidays})


@login_required(login_url='home')
def add_holiday(request):
    if request.POST:
        form = add_holiday_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'holiday_success.html')
    else:

        form = add_holiday_form()
    return render(request, 'add_holiday_form.html', {'form': form})


@login_required(login_url='home')
def update_holiday(request, holiday_id):
    if request.method == 'POST':
        holidays = holiday.objects.get(id=holiday_id)
        form = add_holiday_form(request.POST, instance=holidays)
        if form.is_valid():
            form.save()
            return render(request, 'holiday_success.html')

    else:
        minute = holiday.objects.get(id=holiday_id)
        form = add_holiday_form(instance=minute)
    return render(request, 'add_holiday_form.html', {'form': form})


@login_required(login_url='home')
def drop_holiday(request, holiday_id):
    delete_holiday = holiday.objects.get(id=holiday_id)
    delete_holiday.delete()
    return render(request, 'delete_holiday_success.html')
