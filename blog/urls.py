from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resources/$', views.guides, name='resources'),
    url(r'^success_blog/$', views.success_blog, name='success_blog'),
    url(r'^(?P<slug>[\w\-]+)/$', views.story),
]