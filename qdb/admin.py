# -*- coding: utf-8 -*-
from django.contrib import admin
from qdb.models import Quote


class QAdmin(admin.ModelAdmin):
    list_display = ('id', 'pievienots', 'apstiprinats', '__unicode__',)
    list_filter = ('apstiprinats',)
    search_fields = ('teksts',)

admin.site.register(Quote, QAdmin)
# from django.contrib.comments.admin import CommentAdmin
# from django.contrib.comments.models import Comment
# admin.site.register(Comment, CommentAdmin)
