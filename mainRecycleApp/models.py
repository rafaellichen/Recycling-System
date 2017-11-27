# -*- coding: utf-8 -*-
'''Models for MainRecycleApp contains RecyclingCenter model'''
from __future__ import unicode_literals

from django.db import models

class RecyclingCenter(models.Model):
    '''Model for RecyclingCenters in searchResult App'''
    name = models.TextField()
    address = models.TextField()
    recycleType = models.TextField()
    monday = models.TextField()
    tuesday = models.TextField()
    wednesday = models.TextField()
    thrusday = models.TextField()
    friday = models.TextField()
    saturday = models.TextField()
    sunday = models.TextField()
    borough = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    phone = models.TextField()
    picks_up = models.TextField()
    website = models.TextField()

    def __str__(self):
        '''Method to return the string name'''
        return self.name
