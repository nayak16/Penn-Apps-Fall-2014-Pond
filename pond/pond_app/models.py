from django.db import models
#from django_mongodb_engine.storage import GridFSStorage
from djangotoolbox.fields import EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

#gridfs = GridFSStorage()

# Create your models here.


class Location(models.Model):
        latitude = models.FloatField()
        longitude = models.FloatField()


class FileUpload(models.Model):
	title = models.CharField(max_length=64, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	expiration_time = models.IntegerField()
	file = models.FileField(upload_to='pond_collections/')
	author = models.ForeignKey(UserProfile,null=True)
	location = EmbeddedModelField(Location, null=True)
	radius_meters = models.FloatField(null=True)
	is_protected = models.NullBooleanField(null=True)
	password = models.CharField(max_length=255)
	objects=MongoDBManager()
	access_count = models.IntegerField()
	file_type = models.CharField(max_length=8)

	@property
	def filename(self):
		return self.file.name.rsplit('/', 1)[-1]