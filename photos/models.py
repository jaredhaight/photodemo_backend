from django.db import models
from django.contrib.auth.models import User
from photos.photoutils import resize_image, get_orientation, get_exif, make_thumbnail
from django.core.files import File

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    desc = models.CharField(max_length=1024, blank=True)
    exif_iso = models.CharField(max_length=10, editable=False, null=True, blank=True)
    exif_aperture = models.CharField(max_length=10, editable=False, null=True, blank=True)
    exif_shutter = models.CharField(max_length=10, editable=False, null=True, blank=True)
    exif_focal = models.CharField(max_length=10, editable=False, null=True, blank=True)
    exif_date_taken = models.DateTimeField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='photos')
    raw_file = models.FileField(upload_to='raws', null=True, blank=True)
    orientation = models.CharField(max_length=20, editable=False, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    permissions = models.CharField(max_length=1024, null=True, blank=True)
    author = models.ForeignKey(User, related_name='photo')
    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title == '':
            self.title = self.image.name.strip('photos/')
        if self.title is None:
            self.title = self.image.name.strip('photos/')
        if self.permissions is None:
            self.permissions = 'private'
        super(Photo, self).save(*args, **kwargs)
        self.orientation = get_orientation(self.image)
        #Get EXIF
        exif = get_exif(self.image)
        self.exif_aperture = exif['aperture']
        self.exif_date_taken = exif['date_taken']
        self.exif_focal = exif['focal']
        self.exif_iso = exif['iso']
        self.exif_shutter = exif['shutter']
        #Commit changes to photo object
        super(Photo, self).save()
        #Photo is saved now, lets create crops.
        crops = Crop.objects.filter(photo=self)
        if crops.count() == 0:
            thumbnail = make_thumbnail(self.image, 400, 400)
            openthumb = File(open(thumbnail))
            Crop.objects.create(desc='thumbnail', photo=self, width=400, height=0, image=openthumb, permissions='Public')
            thumbnail = resize_image(self.image, 0, 2048)
            openthumb = File(open(thumbnail))
            Crop.objects.create(desc='display', photo=self, width=2048, height=0, image=openthumb, permissions='Public')


class Crop(models.Model):
    desc = models.CharField(max_length=1024)
    photo = models.ForeignKey('Photo', related_name='crops', null=True, blank=True)
    width = models.IntegerField(max_length=5, null=True, blank=True)
    height = models.IntegerField(max_length=5, null=True, blank=True)
    image = models.ImageField(upload_to='crops', null=True, blank=True)
    permissions = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        if self.image:
            image = self.image
        else:
            image = 'Null'
        return '%s: %s' % (self.desc, str(image.url))