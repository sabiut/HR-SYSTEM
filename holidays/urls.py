from . import views
from django.urls import path

urlpatterns = [
    path(r'holidays/', views.holidays, name='holidays'),
    path(r'view_holidays_hr/', views.view_holidays_hr, name='view_holidays_hr'),
    path(r'add_holiday/', views.add_holiday, name='add_holiday'),
    path(r'<int:holiday_id>/edit_holiday/', views.update_holiday, name='update_holiday'),
    path(r'<int:holiday_id>/delete_holiday/', views.drop_holiday, name='drop_holiday')

]
