from django.shortcuts import render, redirect
from forms import UploadedFile

from django.utils import timezone

from models import UploadedFile

#from share.forms import UploadedFile
# Create your views here.


def index(request):

    return render(request, 'index.html', {})


def upload_file(request):

    new_file = UploadedFile()
    #new_file.time_uploaded = timezone.now()
    new_file.file = request.POST['file']
    new_file.save()
    return redirect('index')


#def _upload_file(request):

    #if request.method == 'POST':
    	#form = UploadedFile(request.POST, request.FILES)
    	#if form.is_Valid():
    		#handle_uploaded_file(request.FILES['file'])
    		#return redirect('index')
    #se:
    	#form = UploadedFile()
    #return redirect('index')


#def handle_uploaded_file(f):
    #with open('some/file/name.txt', 'wb+') as destination:
        #for chunk in f.chunks():
            #destination.write(chunk)
