import re

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django import template
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from pond_app.models import Location, FileUpload, UserProfile
from mimetypes import guess_type

# from gridfsuploads import gridfs_storage
import gridfs
from gridfs.errors import NoFile

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
    return render(request,'../static/index.html', context)

