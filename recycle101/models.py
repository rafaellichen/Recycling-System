from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HowTo(models.Model):
    """
    Model for the Safe Disposal Events
    """
    recycleType = models.TextField()
    description = models.TextField()

    def __str__(self):
        """
        Method to return the name
        """
        return self.recycleType
