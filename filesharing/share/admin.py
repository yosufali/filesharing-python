from django.contrib import admin
#from share.forms import UploadedFile
from share.models import File

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name", "file_link"]

admin.site.register(File, FileAdmin)