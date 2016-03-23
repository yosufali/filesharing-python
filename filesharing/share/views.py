from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils import timezone

from share.models import File
from share.forms import FileForm

from datetime import timedelta

def index(request):

    return render(request, 'index.html', {})

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = File(file=request.FILES['file'])
            newfile.name = request.FILES['file'].name

            dur = request.POST['duration']
            newfile.duration = get_duration(dur)
            newfile.save()

            # Redirect to the file list after POST
            return HttpResponseRedirect(reverse('upload'))
    else:
        form = FileForm()  # A empty, unbound form

    # Load file for the list page
    files = File.objects.all()

    # Render list page with the files
    return render_to_response(
        'list.html',
        {'files': files, 'form': form},
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
    return 0
