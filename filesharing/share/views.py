from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils import timezone

from share.models import File
from share.forms import FileForm

# Create your views here.

def index(request):

    return render(request, 'index.html', {})

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = File(file=request.FILES['file'])
            newfile.name = request.FILES['file'].name
            newfile.save()

            # Redirect to the file list after POST
            return HttpResponseRedirect(reverse('upload'))
            #return redirect('index')
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

