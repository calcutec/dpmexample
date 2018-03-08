from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^form/', include('release.urls')),
]
