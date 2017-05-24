# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from qdb.models import Quote


class LatestPearlsFeed(Feed):
    title = u"Jaunākās pērles"
    link = "latest/feed/"
    description = u"Lodesmuiza.lv pērļu krātuves 20. jaunākās pērles."

    def items(self):
        return Quote.objects.filter(apstiprinats__exact=True).order_by('-id')[:20]

    def item_title(self, item):
        return u'%d - %s... (%s)' % (item.id, item.teksts[:20], item.pievienots)

    def item_description(self, item):
        return item.teksts
    
    def item_link(self, item):
        return '%d' % item.id
