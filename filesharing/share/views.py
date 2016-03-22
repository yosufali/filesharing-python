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

# def upload_file(request):

#     new_file = UploadedFile()
#     #new_file.time_uploaded = timezone.now()
#     new_file.file = request.POST['file']
#     new_file.save()
#     return redirect('index')

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = File(file=request.FILES['file'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('upload'))
            #return redirect('index')
    else:
        form = FileForm()  # A empty, unbound form

    # Load documents for the list page
    files = File.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
    )