from . import views
from django.urls import path

urlpatterns = [
    path(r'medical_scheme_form/', views.medical_scheme_form, name="medical_form"),
    path(r'all_medical_details/', views.all_medical_details, name='all_medical_details'),
    path(r'<int:staffs_id>/fc_processing_form/', views.Financial_controller_process_medical_details,
         name='processing_form'),
    path(r' processed_medical_details/', views.processed_medical_details, name='processed_medicals'),
    path(r'processed_medical_details_profile/', views.processed_medical_details_profile,
         name='processed_medical_details_profile'),
    path(r'processed_medical_details_director/', views.processed_medical_details_director,
         name='processed_medical_details_director')

]
