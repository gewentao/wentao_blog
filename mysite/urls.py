from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import mainPage
from blog.views import postPage
from blog.views import archivePage
from blog.views import galleryPage
from blog.views import aboutPage

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':'media'}),
    url(r'^blog_admin', include(admin.site.urls)),
    url(r'^$',mainPage),
    url(r'^archive/$',archivePage),
    url(r'^gallery/$',galleryPage),
    url(r'^about/$',aboutPage),
    url(r'^blog/post',postPage),
)
