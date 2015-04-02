from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FormsWithFriends.views.landing', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'FormsWithFriends.views.register', name='register'),
    url(r'^about/$', 'FormsWithFriends.views.aboutus', name='about'),
    url(r'^login/$', 'FormsWithFriends.views.login', name='login'),
    url(r'^logout/$', 'FormsWithFriends.views.logout', name='logout'),
    
    url(r'^templates/create/$', 'templates.views.createTemplate', name='createTemplate'),
    url(r'^templates/index/$', 'templates.views.userIndexTemplate', name='userIndexTemplate'),
    url(r"^templates/view/(?P<template_id>\d+)/$", 'templates.views.viewTemplate', name='viewTemplate'),
    url(r"^questions/create/(?P<template_id>\d+)/$", 'templates.views.createQuestion', name='createQuestion'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )