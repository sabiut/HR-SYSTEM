from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'sick_leave_application/', views.sick_leave_application, name="sick_leave_application"),
    path(r'display_sick_leave/', views.display_sick_leave, name="display_sick_leave"),
    path(r'update_sick_leave_balance/', views.update_sick_leave_balance, name='update_sick_leave_balance'),
    # path(r'calculate_sick_leave_balance/', views.calculate_sick_leave_balance, name='calculate_sick_leave_balance'),
    path(r'display_sick_leave_Authorizer_page/', views.display_sick_leave_Authorizer_page,
         name='display_sick_leave_Authorizer_page'),
    # path(r'display_sick_leave_Director_Authorizer_page/', views.display_sick_leave_Director_Authorizer_page,
    #      name='sick_to_approved_by_director'),
    path(r'display_approved_sick_leaves/', views.display_approved_sick_leaves, name='approved_sick_leaves'),
    path(r'sick_leave_pending_director_approval/', views.sick_leave_pending_director_approval,
         name='sick_leave_pending_director_approval'),
    # path(r'display_approved_sick_leaves_authorizer_page/', views.display_approved_sick_leaves_authorizer_page,
    #      name='display_approved_sick_leaves_authorizer_page'),
    # path(r'display_sick_leave_governor_page/', views.display_sick_leave_governor_page,
    #      name='display_sick_leave_governor_page'),
    # path(r'display_approved_sick_leaves_governor_page/', views.display_approved_sick_leaves_governor_page,
    #      name='display_approved_sick_leaves_governor_page')
    path(r'sick_to_approved_by_director/', views.sick_to_approved_by_director, name='sick_to_approved_by_director')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
