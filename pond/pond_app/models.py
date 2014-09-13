from django.db import models
from django_mongodb_engine.storage import GridFSStorage
from djangotoolbox.fields import EmbeddedModelField

gridfs = GridFSStorage()

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    def __str__(self):
        return "%s's profile" % self.user


class Location(models.Model):
        latitude = models.FloatField()
        longitude = models.FloatField()


class FileUpload(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField()
    file = models.FileField(storage=gridfs, upload_to='/')
    author = models.ForeignKey(UserProfile)
    location = EmbededModelField(Location)
    radius_meters = models.FloatField()
    is_protected = models.BooleanField()
    password = models.CharField(max_length=255)
