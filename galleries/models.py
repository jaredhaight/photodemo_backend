__author__ = 'jared'
from django.db import models
from photos.models import Photo

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=1024, blank=True)
    photos = models.ManyToManyField(Photo, related_name='photos')
    permissions = models.CharField(max_length=1024)