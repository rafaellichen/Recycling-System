# -*- coding: utf-8 -*-
'''Models for MainRecycleApp contains RecyclingCenter model'''
from __future__ import unicode_literals

from django.db import models

class RecyclingCenter(models.Model):
    '''Model for RecyclingCenters in searchResult App'''
    idc = models.TextField()
    name = models.TextField()
    address = models.TextField()
    type = models.TextField()
    Monday = models.TextField()
    Tuesday = models.TextField()
    Wednesday = models.TextField()
    Thursday = models.TextField()
    Friday = models.TextField()
    Saturday = models.TextField()
    Sunday = models.TextField()
    #recycleType = models.TextField()
    borough = models.TextField()
    zip = models.TextField()
    cell = models.TextField()
    picksup = models.TextField()
    url = models.TextField()
    #website = models.TextField()
    #logo_url = models.TextField()

    def __str__(self):
        '''Method to return the string name'''
        return self.name
