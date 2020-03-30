from . import views
from django.urls import path

urlpatterns = [
    path('my_personal_info/', views.my_personal_info, name="my_personal_info"),
    path('edit_my_personal_info/', views.edit_my_personal_info, name="edit_my_personal_info"),
    path('edit_emergency/', views.edit_emergency, name='edit_emergency'),
    path('authorizer_personal_info/', views.authorizer_personal_info, name='authorizer_personal_info'),
    path('director_personal_info/', views.director_personal_info, name='director_personal_info'),
    path('hr_personal_info/', views.hr_personal_info, name='hr_personal_info'),
    path('add_staff_personal_info/', views.add_staff_personal_info, name='add_staff_personal_info'),
    path('add_staff_education_level/', views.add_staff_education_level, name='add_staff_education_level'),
    path('add_staff_emergency/', views.add_staff_emergency, name='add_staff_emergency'),
    path('add_family_dependants/', views.add_family_dependants, name='add_family_dependants'),
    path('add_job_history/', views.add_job_history, name='add_job_history'),
    path('all_staff_personal_info/', views.all_staff_personal_info, name='all_staff_personal_info'),
    path('query_personal_info/', views.query_personal_info, name='query_personal_info'),
    path('all_education_history/', views.all_education_history, name='all_education_history'),
    path('all_emergency/', views.all_emergency, name='all_emergency'),
    path('all_dependants/', views.all_dependants, name='all_dependants'),
    path('all_Job_History/', views.all_Job_History, name='all_Job_History'),
    path('<int:id>/edit_personal_info', views.edit_personal_info, name='edit_personal_info'),
    path(r'<int:profile_id>/delete_profile/', views.drop_personal_info, name='profile'),
    path('<int:id>/edit_staff_education/', views.edit_staff_education, name='edit_staff_education'),
    path(r'<int:profile_id>/delete_staff_education/', views.drop_staff_education, name='drop_staff_education'),
    path(r'<int:id>/add_emergency/', views.edit_staff_emergency, name='edit_staff_emergency'),
    path(r'<int:profile_id>/delete_emergency/', views.drop_staff_emergency, name='drop_staff_emergency'),
    path(r'<int:id>/add_dependant/', views.edit_staff_dependent, name='edit_staff_dependent'),
    path(r'<int:profile_id>/delete_dependant/', views.drop_staff_dependent, name='drop_staff_dependent'),
    path(r'<int:id>/edit_job_history/', views.edit_staff_job_history, name='edit_staff_job_history'),
    path(r'<int:profile_id>/delete_job_history/', views.drop_staff_job_history, name='drop_staff_job_history'),




]
