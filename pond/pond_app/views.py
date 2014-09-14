import re

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django import template
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from pond_app.models import *
from pond_app.forms import *
from mimetypes import guess_type

# from gridfsuploads import gridfs_storage
import gridfs
from gridfs.errors import NoFile


from filetransfers.api import prepare_upload, serve_file

def upload_handler(request):
    view_url = reverse('upload.views.upload_handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(view_url)

    print 'hello'
    upload_url, upload_data = prepare_upload(request, view_url, private=True)
    form = UploadForm()
    return direct_to_template(request, 'upload/upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data,
         'uploads': UploadModel.objects.all()})

def serve_from_gridfs(request,id):

    try:
        gridfile=gridfs_storage.open(path)
    except NoFile:
        raise Http404
    else:
        return HttpResponse(gridfile,mimetype=guess_type(path)[0])


#def upload_to_gridfs(request,path):


def home(request):
    context={}
    error=[]
    context["errors"]=error

    return render(request,'test.html', context)


