# -*- coding: utf-8 -*-
from django import http
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from qdb.models import Quote


def single(request, quote_id):
    u"""Parāda vienu pērli"""
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'qdb/single.html', {'quote': quote})


def no(request):
    u"""Galvenā lapa, kura arī saprot, ja padod PK"""
    quote_id = request.GET.get('quote_id')
    if quote_id:
        return http.HttpResponseRedirect(reverse('qdb.views.single', args=[quote_id]))
    else:
        return render(request, 'qdb/main.html')


def vote(request, quote_id):
    u"""Balsošanas skats"""
    quote = get_object_or_404(Quote, pk=quote_id)
    up = request.POST.get('up', False)
    down = request.POST.get('down', False)
    if up:
        quote.balsis += 1
        quote.punkti += 1
    if down:
        quote.balsis += 1
        quote.punkti -= 1
    quote.save()
    return render(request, 'qdb/updated.html', {'quote': quote})


def random(request):
    u"""Ieber man sauju pērļu"""
    quotes = Quote.objects.filter(apstiprinats__exact=True).order_by('?')[:20]
    return render(request, 'qdb/random.html', {'quotes': quotes})


def top10(request):
    u"""Pērles ar visaugstāko vērtējumu"""
    quotes = Quote.objects.filter(apstiprinats__exact=True).order_by('-punkti')[:10]
    return render(request, 'qdb/top10.html', {'quotes': quotes})


def latest(request):
    u"""Jaunākās pērles"""
    quotes = Quote.objects.filter(apstiprinats__exact=True).order_by('-id')[:20]
    return render(request, 'qdb/latest.html', {'quotes': quotes})


def about(request):
    return render(request, 'qdb/about.html')
