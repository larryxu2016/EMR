"""
Definition of urls for EMR.
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('login.urls')),
    url(r'^patientcontact/', include('patientcontact.urls')),
    url(r'^patientmedicalhistory/', include('patientmedicalhistory.urls')),
    url(r'^patientinsurance/', include('patientinsurance.urls')),
    url(r'^patientmeds/', include('patientmeds.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
]
