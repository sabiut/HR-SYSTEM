from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from login.models import *
from personal_info.forms import *


@login_required(login_url='home')
def my_personal_info(request):
    if request.user.is_authenticated:
        get_user = request.user
        profile = Profile.objects.filter(user=request.user)
        education = education_history.objects.filter(user=request.user)
        emergency_data = emergency.objects.filter(user=request.user)
        dependant = Family_and_Dependants.objects.filter(user=request.user)
        job = Job_History.objects.filter(user=request.user)
        return render(request, 'my_personal_info.html', locals())


@login_required(login_url='home')
def authorizer_personal_info(request):
    if request.user.is_authenticated:
        get_user = request.user
        profile = Profile.objects.filter(user=request.user)
        education = education_history.objects.filter(user=request.user)
        emergency_data = emergency.objects.filter(user=request.user)
        dependant = Family_and_Dependants.objects.filter(user=request.user)
        job = Job_History.objects.filter(user=request.user)
        return render(request, 'authorizer_personal_info.html', locals())
    else:
        return HttpResponse('Please ensure that the personal information is update')


@login_required(login_url='home')
def director_personal_info(request):
    if request.user.is_authenticated:
        get_user = request.user
        profile = Profile.objects.filter(user=request.user)
        education = education_history.objects.filter(user=request.user)
        emergency_data = emergency.objects.filter(user=request.user)
        dependant = Family_and_Dependants.objects.filter(user=request.user)
        job = Job_History.objects.filter(user=request.user)
        return render(request, 'director_personal_info.html', locals())


@login_required(login_url='home')
def hr_personal_info(request):
    if request.user.is_authenticated:
        get_user = request.user
        profile = Profile.objects.filter(user=request.user)
        education = education_history.objects.filter(user=request.user)
        emergency_data = emergency.objects.filter(user=request.user)
        dependant = Family_and_Dependants.objects.filter(user=request.user)
        job = Job_History.objects.filter(user=request.user)
        return render(request, 'hr_personal_info.html', locals())


@login_required(login_url='home')
def edit_my_personal_info(request):
    try:
        profile = request.user.profile
    except:
        return HttpResponse('User does mot have the profile information.\n Please complete the profile information '
                            'and try again')
        profile = Profile(user=request.user)
    if request.method == 'POST':

        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'success.html')

        else:
            message.error(request, 'Please correct the error and try again')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update_personal_info.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required(login_url='home')
def edit_emergency(request):
    try:
        emergency = request.user.emergency
    except:
        return HttpResponse('User does mot have the emergency information.\n Please complete the emergency information '
                            'and try again')
        emergency = emergency(user=request.user)
    if request.method == 'POST':
        profile_form = EmergencyForm(request.POST, instance=request.user.emergency)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'success.html')

        else:
            return HttpResponse('Please ensure that the personal information is update')

    else:
        profile_form = EmergencyForm(instance=request.user.emergency)
    return render(request, 'update_personal_info.html', {
        'profile_form': profile_form
    })


@login_required(login_url='home')
def add_staff_personal_info(request):
    if request.method == 'POST':
        profile_form = add_ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'success.html')
    else:
        profile_form = add_ProfileForm()
    return render(request, 'add_personal_info_form.html', {'profile_form': profile_form})


@login_required(login_url='home')
def add_staff_education_level(request):
    if request.method == 'POST':
        profile_form = add_education_history(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'success_message.html')
    else:
        profile_form = add_education_history()
    return render(request, 'add_education_level_form.html', {'profile_form': profile_form})


@login_required(login_url='home')
def add_staff_emergency(request):
    if request.method == 'POST':
        profile_form = add_staff_emergency_Form(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'success_message.html')
    else:
        profile_form = add_staff_emergency_Form()
    return render(request, 'add_staff_emergency_form.html', {'profile_form': profile_form})


@login_required(login_url='home')
def add_family_dependants(request):
    if request.method == 'POST':
        profile_form = add_family_dependant_Form(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'success_message.html')
    else:
        profile_form = add_family_dependant_Form()
    return render(request, 'add_staff_emergency_form.html', {'profile_form': profile_form})


@login_required(login_url='home')
def add_job_history(request):
    if request.method == 'POST':
        profile_form = add_job_history_Form(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'success_message.html')
    else:
        profile_form = add_job_history_Form()
    return render(request, 'add_staff_emergency_form.html', {'profile_form': profile_form})


@login_required(login_url='home')
def query_personal_info(request):
    if "sel_an_option" in request.POST:
        selected_option = request.POST["sel_an_option"]
        if selected_option == 'Personal info':
            return HttpResponseRedirect('/all_staff_personal_info')
        elif selected_option == 'Education':
            return HttpResponseRedirect('/all_education_history')
        elif selected_option == 'Emergency':
            return HttpResponseRedirect('/all_emergency')

        elif selected_option == 'Dependants':
            return HttpResponseRedirect('/all_dependants')
        elif selected_option == 'Job History':
            return HttpResponseRedirect('/all_Job_History')


@login_required(login_url='home')
def all_staff_personal_info(request):
    personal_info = Profile.objects.all()
    return render(request, 'all_staff_personal_info.html', {'personal_info': personal_info})


@login_required(login_url='home')
def all_education_history(request):
    personal_info = education_history.objects.all()
    return render(request, 'all_education.html', {'personal_info': personal_info})


@login_required(login_url='home')
def all_emergency(request):
    personal_info = emergency.objects.all()
    return render(request, 'staff_emergency.html', {'personal_info': personal_info})


@login_required(login_url='home')
def all_dependants(request):
    personal_info = Family_and_Dependants.objects.all()
    return render(request, 'dependants.html', {'personal_info': personal_info})


@login_required(login_url='home')
def all_Job_History(request):
    personal_info = Job_History.objects.all()
    return render(request, 'job_history.html', {'personal_info': personal_info})


@login_required(login_url='home')
def edit_personal_info(request, id):
    if request.method == 'POST':
        get_id = Profile.objects.get(id=id)
        form = add_ProfileForm(request.POST, instance=get_id)
        if form.is_valid():
            form.save()
            return render(request, 'success_message.html')

    else:
        get_id = Profile.objects.get(id=id)
        form = add_ProfileForm(instance=get_id)
    return render(request, 'update_data_form.html', {'form': form})


@login_required(login_url='home')
def drop_personal_info(request, profile_id):
    delete_profile = Profile.objects.get(id=profile_id)
    delete_profile.delete()
    return HttpResponseRedirect('/all_staff_personal_info')


@login_required(login_url='home')
def edit_staff_education(request, id):
    if request.method == 'POST':
        get_id = education_history.objects.get(id=id)
        form = add_education_history(request.POST, instance=get_id)
        if form.is_valid():
            form.save()
            return render(request, 'success_message.html')

    else:
        get_id = education_history.objects.get(id=id)
        form = add_education_history(instance=get_id)
    return render(request, 'update_data_form.html', {'form': form})


@login_required(login_url='home')
def drop_staff_education(request, profile_id):
    delete_profile = education_history.objects.get(id=profile_id)
    delete_profile.delete()
    return HttpResponseRedirect('/all_education_history')


@login_required(login_url='home')
def edit_staff_emergency(request, id):
    if request.method == 'POST':
        get_id = emergency.objects.get(id=id)
        form = add_staff_emergency_Form(request.POST, instance=get_id)
        if form.is_valid():
            form.save()
            return render(request, 'success_message.html')

    else:
        get_id = emergency.objects.get(id=id)
        form = add_staff_emergency_Form(instance=get_id)
    return render(request, 'update_data_form.html', {'form': form})


@login_required(login_url='home')
def drop_staff_emergency(request, profile_id):
    delete_profile = emergency.objects.get(id=profile_id)
    delete_profile.delete()
    return HttpResponseRedirect('/all_emergency')


@login_required(login_url='home')
def edit_staff_dependent(request, id):
    if request.method == 'POST':
        get_id = Family_and_Dependants.objects.get(id=id)
        form = add_family_dependant_Form(request.POST, instance=get_id)
        if form.is_valid():
            form.save()
            return render(request, 'success_message.html')

    else:
        get_id = Family_and_Dependants.objects.get(id=id)
        form = add_family_dependant_Form(instance=get_id)
    return render(request, 'update_data_form.html', {'form': form})


@login_required(login_url='home')
def drop_staff_dependent(request, profile_id):
    delete_profile = Family_and_Dependants.objects.get(id=profile_id)
    delete_profile.delete()
    return HttpResponseRedirect('/all_dependants')


@login_required(login_url='home')
def edit_staff_job_history(request, id):
    if request.method == 'POST':
        get_id = Job_History.objects.get(id=id)
        form = add_job_history_Form(request.POST, instance=get_id)
        if form.is_valid():
            form.save()
            return render(request, 'success_message.html')

    else:
        get_id = Job_History.objects.get(id=id)
        form = add_job_history_Form(instance=get_id)
    return render(request, 'update_data_form.html', {'form': form})


@login_required(login_url='home')
def drop_staff_job_history(request, profile_id):
    delete_profile = Job_History.objects.get(id=profile_id)
    delete_profile.delete()
    return HttpResponseRedirect('/all_dependants')
