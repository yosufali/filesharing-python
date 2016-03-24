from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse

from django.utils import timezone

from share.models import File
from share.forms import FileForm

from datetime import timedelta

import random, string

def index(request):

    return render(request, 'index.html', {})

def upload_file(request):
    # Handle file upload
    newfile = File()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = File(file=request.FILES['file'])
            newfile.name = request.FILES['file'].name
            newfile.urlname = generate_string()

            dur = request.POST['duration']
            newfile.duration = get_duration(dur)
            newfile.save()

            # Redirect to the file list after POST
            #return HttpResponseRedirect(reverse('upload'))
    else:
        form = FileForm()  # A empty, unbound form

    return render_to_response(
        'yourfile.html',
        {'file': newfile, 'form': form, 'download_url': newfile.urlname},
        context_instance=RequestContext(request)
    )

def get_duration(dur):
    durations = {
        '5m' : timedelta(minutes=5),
        '1h' : timedelta(hours=1),
        '6h' : timedelta(hours=6),
        '24h' : timedelta(days=1),
        '3d' : timedelta(days=3)
    }

    for d in durations:
        if d == dur:
            return durations[d]
    return timedelta()

def generate_string():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(10))

def serve_download_page(request, urltext):
    
    file_to_download = File.objects.get(urlname=urltext)

    if file_to_download != None:
        return render_to_response('download.html', {'download' : file_to_download}, context_instance=RequestContext(request))
    else:
        return HttpResponseNotFound('Nothing here soz')
