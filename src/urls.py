"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'', include('login.urls')),
    path(r'', include('leaveform.urls')),
    path(r'', include('authorize_leave.urls')),
    # path(r'', include('Hr_office.urls')),
    # path(r'', include('staffinfo.urls')),
    path(r'', include('sickleave.urls')),
    # path(r'', include('staff_balance.urls')),
    # path(r'', include('holidays.urls')),
    # path(r'', include('personal_info.urls')),
    path(r'', include('encashment.urls')),
    # path(r'', include('loans.urls')),
    # path(r'', include('housing_loan.urls')),
    # path(r'', include('medical_scheme.urls'))

]

# customize the administrator text
admin.site.site_header = "Human Resource System"
admin.site.index_title = "Welcome to e-Leave Administrator"
