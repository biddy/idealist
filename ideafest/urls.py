import nodes.urls

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^ideas/', include(nodes.urls, namespace='ideas')),
    url(r'^admin/', include(admin.site.urls)),
)
