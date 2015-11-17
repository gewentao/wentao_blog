from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	abstract = models.TextField() #the abstract (shown in the main page)
	counts = models.IntegerField(default=0) #count the click times
	create_time = models.DateTimeField()
	update_time = models.DateTimeField(blank=True, null=True)
	contain_img = models.BooleanField(default=False)
	contain_mp3 = models.BooleanField(default=False)
	mp3_url = models.CharField(max_length=500, blank=True, null=True) #the url of mp3
	mp3_singer = models.CharField(max_length=500, default="Unknow Artist")
	mp3_name = models.CharField(max_length=500, default="Unknow Song")


class GalleryPost(models.Model):
	title = models.CharField(max_length=150)
	abstract = models.TextField(blank=True, null=True)
	src = models.CharField(max_length=500, blank=True, null=True)# use filename to replace src
	file_name = models.CharField(max_length=500)#eg: test.jpg  the file is saved in /static/gallery_photos/
	view_count = models.IntegerField(default=0)
	create_time = models.DateTimeField()
	camera = models.CharField(max_length=50)
	lens = models.CharField(max_length=50)
	exif = models.CharField(max_length=100)
	position = models.CharField(max_length=100)

class BlogVisit(models.Model):
	blog = models.ForeignKey(BlogPost)
	visit_ip = models.IPAddressField()
	visit_time = models.DateTimeField()

class BlogAdmin(admin.ModelAdmin):
        list_display = ('title','create_time')
        class Media:
		js = (
				'/media/js/tiny_mce/tiny_mce.js',
				'/media/js/textareas.js',
		     )

class GalleryAdmin(admin.ModelAdmin):
        list_display = ('title','create_time')

#admin.site.register(BlogPost)
