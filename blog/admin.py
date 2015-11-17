from django.contrib import admin
from blog.models import BlogPost
from blog.models import GalleryPost
from blog.models import BlogAdmin
from blog.models import GalleryAdmin

admin.site.register(BlogPost,BlogAdmin)
admin.site.register(GalleryPost,GalleryAdmin)
