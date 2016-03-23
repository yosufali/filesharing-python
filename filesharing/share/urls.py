from django.conf.urls import url, include
from . import views

#TODO: Make upload url unique

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^upload/$', views.upload_file, name="upload"),
]