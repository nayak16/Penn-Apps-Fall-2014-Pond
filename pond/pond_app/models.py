from django.db import models
#from django_mongodb_engine.storage import GridFSStorage
from djangotoolbox.fields import EmbeddedModelField

#gridfs = GridFSStorage()

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
	title = models.CharField(max_length=64, blank=True)
	#created_on = models.DateTimeField(auto_now_add=True)
	#expiration_time = models.DateTimeField(auto_now_add=True)
	file = models.FileField(upload_to='pond_collections/')
	#author = models.ForeignKey(UserProfile,null=True)
	#location = EmbeddedModelField(Location, null=True)
	#radius_meters = models.FloatField(null=True)
	#is_protected = models.NullBooleanField(null=True)
	#password = models.CharField(max_length=255)



	@property
	def filename(self):
		return self.file.name.rsplit('/', 1)[-1]