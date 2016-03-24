from django.contrib import admin
#from share.forms import UploadedFile
from share.models import File

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    fields = ["name","uploaded_at", "expires_at", "urlname", "duration"]
    list_display = ["name", "uploaded_at", "duration",  "expires_at", "urlname", "file_link"]

admin.site.register(File, FileAdmin)