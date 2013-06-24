from django.contrib import admin
from galleries.models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)