from django.conf.urls import url

from . import views

app_name = 'patientinsurance'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^saveInsurInfo/$', views.saveInsurInfo, name='saveInsurInfo'),
    url(r'^modifyInsurInfo/$', views.modifyInsurInfo, name='modifyInsurInfo'),
    url(r'^modifypage/$', views.ModifyView.as_view(), name='modifypage'),
    url(r'^modifypage2/$', views.Modify2View.as_view(), name='modifypage2'),
    url(r'^readInsInfo/$', views.readData, name='readInsInfo'),
]