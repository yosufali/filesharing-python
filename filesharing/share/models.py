from __future__ import unicode_literals

from django.utils import timezone

from django.db import models


# Create your models here.


class File(models.Model):

    name = models.CharField(max_length=500)
    date_uploaded = models.DateField(auto_now_add=True)
    time_uploaded = models.TimeField(default=timezone.now)
    #duration = models.DurationField(default=timedelta(minutes=5))
    #expires = models.DateTimeField()
    file = models.FileField(upload_to='files')

    def file_link(self):
		if self.file:
			return "<a href='%s'> Download </a>" % (self.file.url)
		else:
			return "No attatchement"

    file_link.allow_tags = True
