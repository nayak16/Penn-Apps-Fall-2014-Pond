import multiprocessing
import re
import time
import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django import template
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render



from pond_app.forms import *
from pond_app.models import *


from filetransfers.api import prepare_upload, serve_file

def get_nearby(request, lat, lon):
    print "get nearby called motherfucka"
    here = {'latitude' : lat, 'longtitude' : lon}
    
    #nearest=FileUpload.objects.all({'location':{'$near':here}})
    context={ 'uploads': FileUpload.objects.all()}
    
    
    
    return render(request,"upload.html",context)

def upload_no_location(request):
	pass

def upload_handler(request, lat, lon):
    assert(request.method == 'POST')
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect("/home")
    upload_url, upload_data = prepare_upload(request, "/upload/")
    form = UploadForm()
    return render(request, 'upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data,
         'uploads': FileUpload.objects.all()})

    upload_url, upload_data = prepare_upload(request, view_url)

def download_handler(request, pk):
    upload = get_object_or_404(FileUpload, pk=pk)
    return serve_file(request, upload.file, save_as=True)

def delete_handler(request, pk):
    if request.method == 'POST':
        upload = get_object_or_404(FileUpload, pk=pk)
        upload.file.delete()
        upload.delete()
        return HttpResponse(json.dumps({'deleted': 'true'}), content_type='application/json')

def home(request):
	form = UploadForm()
	context={'form':form}
	return render(request, 'home.html', context)

"""

def remove_if_expired(file_upload):
    if file_upload.expiration_time > datetime.datetime.now():
        os.remove(file_upload.file.filename)

def remove_expired_files():
    map(remove_if_expired, FileUpload.objects.all())

def wait_for_files_to_expire():
    seconds = 1
    while True:
        print 'Checking'
        time.sleep(seconds)
        try:
            remove_expired_files()
        except:
            pass

"""