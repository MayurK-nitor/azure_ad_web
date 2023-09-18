from django.conf import settings
from django.urls import include, path, re_path

from . import views

# msal_urls = views.CustomMsalViews(settings.MS_IDENTITY_WEB).url_patterns()


urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^$', views.login_user, name='login_user'),
    # path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
]
