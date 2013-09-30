from django.conf.urls import patterns, url

from .views import TitleListView, NodeListView


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', NodeListView.as_view(), name='detail'),
    url(r'^$', TitleListView.as_view(), name='list'),
)
