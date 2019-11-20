from django.conf.urls import url
from . import views
from .views import Meds

app_name = 'patientmeds'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/?$', Meds.as_view()),
    url(r'^api/(?P<patientmeds_id>[0-9]+)/?$', Meds.as_view()),
]