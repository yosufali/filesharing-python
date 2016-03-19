from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.


class File(models.Model):

    name = models.CharField(max_length=500)
    time_uploaded = models.DateTimeField(default=timezone.now())
    file = models.FileField(upload_to='files')
