# -*- coding: utf-8 -*-
'''Admin for the MainRecycleApp Django App'''
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mainRecycleApp.models import RecyclingCenter, PublicRecyclingBin, SpecialWasteSite
admin.site.register(RecyclingCenter)
admin.site.register(PublicRecyclingBin)
admin.site.register(SpecialWasteSite)
