from django.conf.urls import patterns, include, url
from photodemo_backend.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photodemo_backend.views.home', name='home'),
    # url(r'^photodemo_backend/', include('photodemo_backend.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)

if ENVIRONMENT == 'DEV':
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
            }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes':True}),
    )
