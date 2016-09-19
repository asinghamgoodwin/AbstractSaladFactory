from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import salads.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^salads/', include('salads.urls')),
   # url(r'^db', salads.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
