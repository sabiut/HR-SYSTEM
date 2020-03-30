from . import views
from django.urls import path

urlpatterns = [
    path(r'archivedLeaves/', views.archivedLeaves, name="archived_leaves"),
    path(r'approvedLeaves/', views.approvedLeaves, name="approved_leaves"),
    path(r'rejectedLeaves/', views.rejectedLeaves, name="rejected_leaves"),
    path(r'<int:leave_id>/archived/', views.hr_archive_leave, name="add_to_archive"),
    path(r'allStaffLeaves/', views.allStaffLeaves, name="all_staff_leaves"),
    path(r'staff_balances/', views.staff_balances, name="staff_balances"),
    path(r'update_monthly_entitlement/', views.update_monthly_entitlement, name="monthly_entitlement"),
    path(r'monthly_query/', views.monthly_query, name="query_the_month"),
    path(r'monthly_leave_taken/', views.monthly_leave_taken, name="monthly_leave_taken"),
    path(r'select_an_option/', views.select_an_option, name="select_an_option"),
    path(r'select_leave_and_department/', views.select_leave_and_department, name='select_leave_and_department'),
    path(r'Sick_leave_report/', views.Sick_leave_report, name='Sick_leave_report'),
    path(r'download_sick_leaves/', views.download_sick_leaves, name='download_sick_leaves'),
    path(r'<int:staff_id>/sick_leave', views.display_sick_leave_by_id, name='display_sick_leave_by_id'),
    path(r'download_annual_leaves/', views.download_annual_leaves, name='download_annual_leaves'),
    path(r'Annual_leave_report/', views.Annual_leave_report, name='Annual_leave_report'),
    path(r'<int:staff_id>/annual_leave', views.display_annual_leave_by_id, name='display_annual_leave_by_id'),
    path(r'<int:staffs_id>/update_leave/', views.update_leave_form, name='update_leave_form'),
    path(r'<int:staffs_id>/update_sick_leave/', views.update_sick_leave_form, name='update_sick_leave')

]
