from django.urls import path
from . import views
from .views import CustomResetPasswordView

urlpatterns = [
    path(r'', views.home, name='home'),
    path('login_user/', views.login_user, name="login_user"),
    path('reset_password/', CustomResetPasswordView.as_view(), name='reset_password'),
    path('director_page/', views.director_page, name="director_page"),
    path('authorizer_page/', views.authorizer_page, name="authorizes"),
    path('profile_page/', views.profile_page, name="profile_page"),
    path('invalid_page/', views.invalid_page, name="invalid_page"),
    path('log_out/', views.log_out, name="logout"),
    path('hr/', views.hr, name='hr_officer'),


]
