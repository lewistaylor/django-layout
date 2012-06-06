from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^%s(?P<path>.*)$' % (settings.MEDIA_URL[1:]),
                'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT,
                 'show_indexes': True, }
                ),
   )
