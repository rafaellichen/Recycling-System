# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import ListView
from searchResult.models import RecyclingCenters

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=RecyclingCenters.objects.all(), template_name="searchResult/result.html")),
]
