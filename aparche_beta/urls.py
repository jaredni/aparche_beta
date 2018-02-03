from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'aparche_beta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^acs/', include('acs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
