from django.conf.urls import url

from . import views

app_name = 'patientmedicalhistory'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^saveMedHistoryInfo/$', views.saveMedHistory, name='saveMedHistoryInfo'),
    url(r'^readMedHisInfo/$', views.readData, name='readMedHisInfo'),
]