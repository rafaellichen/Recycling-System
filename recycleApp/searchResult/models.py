# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RecyclingCenters(models.Model):
	name = models.TextField()
	address = models.TextField()
	phone = models.TextField()
	website = models.TextField()
	timetable = models.TextField()

	def __str__(self):
		return self.name	

