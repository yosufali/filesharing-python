from django.contrib import admin
#from share.forms import UploadedFile
from share.models import File

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    fields = ["name", "date_uploaded", "time_uploaded"]
    list_display = ["name", "date_uploaded", "time_uploaded", "file_link"]

admin.site.register(File, FileAdmin)