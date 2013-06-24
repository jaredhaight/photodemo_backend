# Create your views here.
from django.contrib.auth.models import User
from django.http import Http404
from photos.models import Photo
from galleries.models import Gallery
from api.serializers import ListPhotoSerializer, PhotoDetailsSerializer, ListGallerySerializer, GalleryDetailsSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONPRenderer, JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'photos': reverse('photo-list', request=request, format=format),
        'galleries': reverse('gallery-list', request=request, format=format)
    })

class ListPhotos(generics.ListCreateAPIView):
    model = Photo
    serializer_class = ListPhotoSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, BrowsableAPIRenderer, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication)

    def pre_save(self, obj):
        obj.author = self.request.user

class PhotoDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotoDetailsSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, BrowsableAPIRenderer)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication)

    def pre_save(self, obj):
        obj.author = self.request.user

class ListGalleries(generics.ListCreateAPIView):
    model = Gallery
    serializer_class = ListGallerySerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, BrowsableAPIRenderer)
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication)

class GalleryDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Gallery
    serializer_class = GalleryDetailsSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, BrowsableAPIRenderer)
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication)
