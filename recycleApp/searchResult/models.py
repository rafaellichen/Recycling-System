# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RecyclingCenters(models.Model):
	name = models.TextField()
	address = models.TextField()
	borough = models.TextField()
	state = models.TextField()
	zipcode = models.TextField()
	phone = models.TextField()
	picks_up = models.TextField()
	recycleType = models.TextField()
	website = models.TextField()

	def __str__(self):
		return self.name	

