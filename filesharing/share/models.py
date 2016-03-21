from __future__ import unicode_literals

from django.db import models


#from datetime import timedelta

# Create your models here.


class File(models.Model):

    #name = models.CharField(max_length=500)
    #time_uploaded = models.DateTimeField()
    #duration = models.DurationField(default=timedelta(minutes=5))
    #expires = models.DateTimeField()
    file = models.FileField(upload_to='files')
