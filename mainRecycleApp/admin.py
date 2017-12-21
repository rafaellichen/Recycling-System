# -*- coding: utf-8 -*-
'''Admin for the MainRecycleApp Django App'''
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mainRecycleApp.models import RecyclingCenter, PublicRecyclingBin, SpecialWasteSite, Event, Zip, Bookmark, Description
admin.site.register(RecyclingCenter)
admin.site.register(PublicRecyclingBin)
admin.site.register(SpecialWasteSite)
admin.site.register(Event)
admin.site.register(Zip)
admin.site.register(Bookmark)
admin.site.register(Description)
