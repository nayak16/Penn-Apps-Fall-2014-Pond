from django.db import models
from django_mongodb_engine.storage import GridFSStorage

gridfs = GridFSStorage()

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
	username = models.CharField(max_length=150)
	
	def __str__(self):
		return "%s's profile" % self.user




class FileUpload(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=gridfs, upload_to='/')