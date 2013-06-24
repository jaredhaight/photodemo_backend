from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from photodemo_backend.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT

urlpatterns = patterns('',
    url(r'^$', 'api.views.api_root'),
    url(r'^photos/$', views.ListPhotos.as_view(), name="photo-list"),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetails.as_view(), name="photo-detail"),
    url(r'^galleries$', views.ListGalleries.as_view(), name='gallery-list'),
    url(r'^galleries/(?P<pk>[0-9]+)$', views.GalleryDetails.as_view(), name='gallery-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-token/', 'rest_framework.authtoken.views.obtain_auth_token')
)

if ENVIRONMENT == 'DEV':
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
            }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes':True}),
        #url(r'^.*', 'photos.views.home'),
    )

urlpatterns = format_suffix_patterns(urlpatterns)