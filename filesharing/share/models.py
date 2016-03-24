from __future__ import unicode_literals

from django.utils import timezone
import datetime

from django.db import models

from datetime import timedelta

# Create your models here.


class File(models.Model):

    name = models.CharField(max_length=500)

    uploaded_at = models.DateTimeField(default=timezone.now)

    duration = models.DurationField(default=timedelta())

    expires_at = models.DateTimeField(default=timezone.now() + timedelta(minutes=5))

    urlname = models.CharField(max_length=10, unique=True)
    file = models.FileField(upload_to='files')

    def file_link(self):
		if self.file:
			return "<a href='%s'> Download </a>" % (self.file.url)
		else:
			return "No attatchement"

    file_link.allow_tags = True
