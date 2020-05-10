from . import views
from django.urls import path

urlpatterns = [
    path('staff_balance/', views.staff_balance, name="staff_balance"),
    path('staff_balances_director/', views.staff_balances_director, name='staff_balances_director'),
    path('staff_sick_leave_balances/', views.staff_sick_leave_balances, name="sick_leave_balances"),
    path(r'staff_balances_authorizer/', views.staff_balances_authorizer, name='staff_balances_authorizer'),
    path(r'staff_sick_leave_balances_authorizer/', views.staff_sick_leave_balances_authorizer,
         name='sick_leave_balance_authorizer'),
    path(r'staff_sick_leave_balances_director/', views.staff_sick_leave_balances_director,
         name='staff_sick_leave_balances_director'),
    path(r'download_staff_balance/', views.download_staff_balance, name='download_staff_balance'),
    path(r' download_staff_sick_balance/', views.download_staff_sick_balance, name='download_staff_sick_balance'),
    path(r'<int:staffs_id>/update_balance/', views.update_staff_balance_form, name='update_balance'),

]
