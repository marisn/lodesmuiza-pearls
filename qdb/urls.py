# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from qdb.feed import LatestPearlsFeed
from qdb.views import no, single, vote, random, top10, latest, about

urlpatterns = [
    url(r'^$', no, name='qdb_no'),
    url(r'^(?P<quote_id>\d*)/$', single, name='qdb_single'),
    url(r'^(?P<quote_id>\d*)/vote/$', vote, name='qdb_vote'),
    url(r'^random/$', random, name='qdb_random'),
    url(r'^top10/$', top10, name='qdb_top10'),
    url(r'^latest/feed/$', LatestPearlsFeed(), name='qdb_latest_feed'),
    url(r'^latest/$', latest, name='qdb_latest'),
    url(r'^about/$', about, name='qdb_about'),
]
