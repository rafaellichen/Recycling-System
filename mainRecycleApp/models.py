"""
Models for MainRecycleApp contains RecyclingCenter model
"""
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class RecyclingCenter(models.Model):
    """
    Model for Donation Centers / Recycling Centers in mainRecycleApp
    Contains the donation centers with estential attributes name, address, type, borough,
    zipcode, phone number, a boolean for pickup status and the web url if available.
    """
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
    borough = models.TextField()
    zip = models.TextField()
    cell = models.TextField()
    picksup = models.TextField()
    url = models.TextField()

    def __str__(self):
        """ Method to return the string name """
        return self.name

class PublicRecyclingBin(models.Model):
    """
    Model for the public recycling bins which contains the information for public bins
    with attributes , borough, site type, address, latitude and longitude
    """
    borough = models.TextField()
    siteType = models.TextField()
    siteName = models.TextField()
    address = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

    def __str__(self):
        """Method to return the string sitename"""
        return self.siteName

class SpecialWasteSite(models.Model):
    """
    Model for the special waste sites
    """
    name = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    location = models.TextField()
    hours = models.TextField()
    url = models.TextField()

    def __str__(self):
        """
        Method to return the name
        """
        return self.name

class Event(models.Model):
    """
    Model for the Safe Disposal Events
    """
    borough = models.TextField()
    time = models.TextField()
    address = models.TextField()
    date = models.TextField()
    description = models.TextField()

    def __str__(self):
        """
        Method to return the name
        """
        return self.borough

class Zip(models.Model):
    """
    Model for the list of zip codes in NY
    """
    zipcode = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    city = models.CharField(max_length=50)

    def __str__(self):
        """
        Method to return the zipcdoe
        """
        return self.zipcode

class Description(models.Model):
    """
    Model for the Further Description and pickup/drop off information if available
    """
    idc = models.CharField(max_length=5, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pickup_info = models.TextField(blank=True)

    def __str__(self):
        """
        Method to return the name
        """
        return self.name

class Bookmark(models.Model):
    """
    Model for User Bookmarks of Donation Sites
    """
    facility = models.TextField()
    user = models.ForeignKey(User, related_name='bookmarks')
