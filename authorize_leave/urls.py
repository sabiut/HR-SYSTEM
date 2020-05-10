from . import views
from django.urls import path

urlpatterns = [
    path(r'Allleaves/', views.Allleaves, name="all_leaves"),
    path(r'<int:staff_id>', views.UnitmanagerFrorm, name='unit_manager'),
    path(r'Tobeapprovebydirector/', views.Tobeapprovebydirector, name='to_be_approved_by_director'),
    path(r'<int:staffs_id>/', views.unitDirectorForm, name='department_director'),
    path(r'approved_leaves/', views.approved_leaves, name='approved_leave'),
    path(r'<int:staff_id>/approve_sick_leave/', views.Unit_manager_approve_sick_Form, name='approve_sick_leave'),
    path(r'<int:staffs_id>/director_approve_sick_leave/', views.unit_Director_authorize_sick_leave_Form,
          name='director_approve_sick_leave'),
    # path(r'send_email_to_Director/', views.send_email_to_Director, name='send_email_to_Director'),
    # path(r'director_send_email_to_staff/', views.director_send_email_to_staff, name='director_send_email_to_staff'),
    # path(r'manager_send_email_to_staff/', views.manager_send_email_to_staff, name='manager_send_email_to_staff'),
    path(r'annual_pending_director_approval/', views.annual_pending_director_approval,
          name='annual_leave_pending_director_approval'),
    path(r'approved_leaves_authorizer_page/', views.approved_leaves_authorizer_page,
          name='approved_leaves_authorizer_page'),
    # path(r'Tobe_approved_by_governor/', views.Tobe_approved_by_governor, name='Tobe_approved_by_governor'),
    # path(r'approved_leaves_governor_page/', views.approved_leaves_governor_page, name='approved_leaves_governor_page')

]
