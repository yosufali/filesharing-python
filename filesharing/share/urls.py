from django.conf.urls import url, include
from . import views

#TODO: Make upload url unique

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^uploaded/', views.upload_file, name="upload"),
    url(r'^download/(?P<urltext>\w+)', views.serve_download_page, name="download"),
]
