# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RecyclingCenters(models.Model):
	name = models.CharField()
	address = models.CharField()
	phone = models.CharField()
	website = models.CharField()
	timetable = models.CharField()

	
