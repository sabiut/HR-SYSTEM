from . import views
from django.urls import path

urlpatterns = [
    path(r'encashment_application/', views.encashment_application, name="encashment_application"),
    path(r'pending_encashments_athorizer/', views.pending_encashments_athorizer, name='pending_encashments_athorizer'),
    path(r'<int:staff_id>/authorize_encashment/', views.director_authorize_encashment, name='authorize_encashment'),
    # path(r'pending_encashments_profile/', views.pending_encashments_profile, name='pending_encashment'),
    path(r'approved_encashments_authorizer/', views.approved_encashments_authorizer,
          name='approved_encashments_authorizer'),
    # path(r'approved_encashments_profile/', views.approved_encashments_profile, name='approved_encashments_profile'),
    # path(r'director_send_encashment_email_to_staff/', views.director_send_encashment_email_to_staff,
    #      name='director_send_encashment_email_to_staff'),
    path(r'financial_controller/', views.financial_controller, name='financial_controller'),
    path(r'all_encashments/', views.all_encashments, name='all_encashments'),
    path(r'<int:staff_id>/processing_encashment/', views.financial_controller_processed_pay, name='process_encashment'),
    path(r'all_processed_encashments/', views.all_processed_encashments, name='all_processed_encashments'),
    # path(r'<int:staff_id>/encashment_report', views.encashment_report, name='encashment_report'),

]

