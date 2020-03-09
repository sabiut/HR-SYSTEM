from . import views
from django.urls import path

urlpatterns = [
    path(r'leave_application/', views.leave_application, name="application_form"),
    path(r'leave_options/', views.leave_options, name="leave_options"),
    path(r'select_leave_type/', views.select_leave_type, name="select_leave_type"),
    # path(r'<int:staff_id>/my_annual_leave', views.display_my_annual_leave, name='display_my_annual_leave'),
    # path(r'<int:staff_id>/my_sick_leave', views.display_my_sick_leave, name='display_my_sick_leave'),
    # path(r'send_email_to_Authorizer/', views.send_email_to_Authorizer, name='send_email_to_Authorizer'),
    # path(r'filter_annual_authorizer/', views.filter_annual_authorizer, name='filter_authorizer'),
    # path(r'filter_sick_authorizer/', views.filter_sick_authorizer, name='filter_sick_authorizer'),
    # path(r'filter_manager_approved_annual_leave/', views.filter_manager_approved_annual_leave,
    #      name='filter_manager_approved_annual_leave'),
    # path(r'manager_approved_sick_leave/', views.manager_approved_sick_leave, name='manager_approved_sick_leave'),
    # path(r'filter_pending_annual_leave_managers/', views.filter_pending_annual_leave_managers,
    #      name='filter_pending_annual_leave_managers'),
    # path(r'filter_approved_manager_annual_leave/', views.filter_approved_manager_annual_leave,
    #      name='filter_approved_manager_annual_leave'),
    # path(r'filter_pending_authorizer_sick_leave/', views.filter_pending_authorizer_sick_leave,
    #      name='filter_pending_authorizer_sick_leave'),
    # path(r'manager_approved_sick_leave_authorizer_page/', views.manager_approved_sick_leave_authorizer_page,
    #      name='authorizer_approved_sick_leaves'),
    # path(r'insufficient_balance/', views.insufficient_balance, name='insufficient_balance'),
    # path(r'filter_pending_annual_leave_directors', views.filter_pending_annual_leave_directors,
    #      name='filter_pending_annual_leave_directors'),
    # path(r'filter_approved_director_annual_leave/', views.filter_approved_director_annual_leave,
    #      name='filter_approved_director_annual_leave'),
    # path(r'filter_pending_director_sick_leave/', views.filter_pending_director_sick_leave,
    #      name='filter_pending_director_sick_leave'),
    # path(r'manager_approved_sick_leave_director_page/', views.manager_approved_sick_leave_director_page,
    #      name='manager_approved_sick_leave_director_page'),
    # path(r'filter_director_annual_leave_governor/', views.filter_director_annual_leave_governor,
    #      name='filter_director_annual_leave_governor'),
    # path(r'filter_director_approved_annual_leave_governor_page/',
    #      views.filter_director_approved_annual_leave_governor_page, name='filter_director_approved_annual_leave_governor_page'),
    # path(r'filter_director_sick_governor_page/', views.filter_director_sick_governor_page,
    #      name='filter_director_sick_governor_page'),
    # path(r'director_approved_sick_leave_governor_page/', views.director_approved_sick_leave_governor_page,
    #      name='director_approved_sick_leave_governor_page'),
    # path(r'filter_manager_annual_leave_governor_page/', views.filter_manager_annual_leave_governor_page,
    #      name ='filter_manager_annual_leave_governor_page'),
    # path(r'filter_manager_approved_annual_leave_governor_page/', views.filter_manager_approved_annual_leave_governor_page,
    #      name='filter_manager_approved_annual_leave_governor_page'),
    # path(r'filter_manager_sick_leave_governor_page/', views.filter_manager_sick_leave_governor_page,
    #      name='filter_manager_sick_leave_governor_page'),
    # path(r'manager_approved_sick_leave_governor_page/', views.manager_approved_sick_leave_governor_page,
    #      name='manager_approved_sick_leave_governor_page')


]
