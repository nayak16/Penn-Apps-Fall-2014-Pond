from django.conf.urls import patterns, include, url
from pond_app.views import *
from django.template import Template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    #url(r'^$', 'pond_app.views.home', name='home'),
    # url(r'^pond/', include('pond.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',home),
    url(r'^upload/$', upload_handler),
   (r'^download/(?P<pk>.+)$', download_handler),
    (r'^delete/(?P<pk>.+)$', delete_handler),
) 

#remove_expired_files()