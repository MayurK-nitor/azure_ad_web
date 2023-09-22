from django.conf import settings
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^$', views.login_user, name='login_user'),
]
