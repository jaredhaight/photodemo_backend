from django.contrib import admin
from photos.models import Photo, Crop

class PhotoAdmin(admin.ModelAdmin):
    pass

class CropAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Crop, CropAdmin)