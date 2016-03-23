from __future__ import unicode_literals

from django.db import models


#from datetime import timedelta

# Create your models here.


class File(models.Model):

    name = models.CharField(max_length=500)
    #time_uploaded = models.DateTimeField()
    #duration = models.DurationField(default=timedelta(minutes=5))
    #expires = models.DateTimeField()
    file = models.FileField(upload_to='files')

    def file_link(self):
		if self.file:
			return "<a href='%s'> Download </a>" % (self.file.url)
		else:
			return "No attatchement"

    file_link.allow_tags = True
