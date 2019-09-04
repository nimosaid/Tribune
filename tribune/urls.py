from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'',include('news.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^api-token-auth/', obtain_auth_token)
]