# coding=utf8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from BlogApp.models import *
from BlogApp import views as index_views
import settings

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^index/$', index_views.get_blog, name='get_list'),
    url(r'^blog/(\d+)/$', 'BlogApp.views.get_detail', name='get_detail'),
    url(r'blog/catagory/(\w+)/$', 'BlogApp.views.get_category', name='get_category'),
)