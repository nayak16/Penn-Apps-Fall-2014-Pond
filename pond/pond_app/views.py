import multiprocessing
import re
import time
import datetime

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
from django.contrib.gis.utils import GeoIP


from pond_app.forms import *
from pond_app.models import *


from filetransfers.api import prepare_upload, serve_file

def upload_handler(request):
 ######## Get User's IP ################
    g = GeoIP()
    client_ip = request.META['REMOTE_ADDR']
    lat,long = g.lat_lon(client_ip)
    print lat,long


    view_url = reverse('pond_app.views.upload_handler')
    if request.method == 'POST':
        print request.POST
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print "Gets here"
            form.save()
        return HttpResponseRedirect(view_url)

    # upload_url, upload_data = prepare_upload(request, view_url, private=True)
    upload_url, upload_data = prepare_upload(request, view_url)

    form = UploadForm()
    return render(request, 'upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data,
         'uploads': FileUpload.objects.all()})

def download_handler(request, pk):
    upload = get_object_or_404(FileUpload, pk=pk)
    return serve_file(request, upload.file, save_as=True)

def delete_handler(request, pk):
    if request.method == 'POST':
        upload = get_object_or_404(FileUpload, pk=pk)
        upload.file.delete()
        upload.delete()
    return HttpResponseRedirect(reverse('pond_app.views.upload_handler'))

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
