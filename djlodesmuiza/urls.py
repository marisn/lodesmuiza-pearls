# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lapas/', include('django.contrib.flatpages.urls')),
    url(r'^qdb/', include('qdb.urls')),
    url(r'^$', RedirectView.as_view(url='/quote/qdb/', permanent=False), name='index'),
]
