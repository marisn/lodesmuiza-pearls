# -*- coding: utf-8 -*-
from django.db import models


class Quote(models.Model):
    u"""Atsevišķs citāts, ap ko griežas visa pasaule"""
    apstiprinats = models.BooleanField(u"Atzīmē šo tiem, kas ir publicējami", default=False)
    teksts = models.TextField(u"Te nāk smieklīgais teksts")
    balsis = models.IntegerField(u"Cik reizes ir par šo balsots", default=0)
    punkti = models.IntegerField(u"Cik punktus pērle ir savākusi", default=0)
    pievienots = models.DateField(u"Kad pievienots datu bāzei", auto_now_add=True)
    
    def __unicode__(self):
        return (u"%s...") % (self.teksts[:30])

    def get_absolute_url(self):
        return '/quote/%s/' % str(self.id)
