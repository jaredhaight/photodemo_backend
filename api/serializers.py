from rest_framework import serializers
from django.contrib.auth.models import User
from photos.models import Photo, Crop
from galleries.models import Gallery


class CropSerializer(serializers.HyperlinkedModelSerializer):
    crop_url = serializers.Field(source='image.url')
    class Meta:
        model = Crop
        fields = ('desc','crop_url')

class PhotoDetailsSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')
    id = serializers.Field()
    crops = CropSerializer(many=True, read_only=True)
    full_photo = serializers.Field(source='image.url')
    height = serializers.Field(source='image.height')
    width = serializers.Field(source='image.width')
    size_in_bytes = serializers.Field(source='image.size')

    class Meta:
        model = Photo

class ListPhotoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    author = serializers.Field(source='author.username')
    crops = CropSerializer(many=True, read_only=True)
    full_photo = serializers.Field(source='image.url')

    class Meta:
        model = Photo
        fields = ('url', 'id', 'title','author', 'crops', 'full_photo', 'image', 'updated', 'created')

class ListGallerySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    photos = serializers.HyperlinkedRelatedField(many=True, view_name='photo-detail')

    class Meta:
        model = Gallery

class GalleryDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    photos = serializers.HyperlinkedRelatedField(many=True, view_name='photo-detail')

    class Meta:
        model = Photo
        fields = ('url', 'id', 'title','desc','photos')