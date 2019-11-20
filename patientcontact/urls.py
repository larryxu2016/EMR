from django.conf.urls import url

from . import views

app_name = 'patientcontact'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^modifypage/$', views.ModifyView.as_view(), name='modifypage'),
    url(r'^readContactInfo/$', views.readData, name='readContactInfo'),
    url(r'^saveContactInfo/$', views.saveContactInfo, name='saveContactInfo'),
    url(r'^updateContactInfo/$', views.updateContactInfo, name='updateContactInfo'),
]