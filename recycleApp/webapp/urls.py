# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
	url(r'^$', views.index, name = 'index')]