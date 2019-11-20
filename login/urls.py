from django.conf.urls import url

from . import views
from django.urls import include, path

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chgpwdpage/$', views.changePwdPage, name='changepwdpage'),
    url(r'^newuser/$', views.newUser, name='newuser'),
    url(r'^login/?$', views.login, name="verify"),
    url(r'^createuser/?$', views.createUser, name="createuser"),
    url(r'^changepwd/?$', views.changePwd, name="changepwd"),
    url(r'^logoff/?$', views.logoff, name="logoff"),
]