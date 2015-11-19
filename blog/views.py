# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import BlogPost
from blog.models import GalleryPost
from blog.models import BlogVisit
from django.http import Http404
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from blog.utils.get_city_by_ip import get_city_by_ip
from django.utils.timezone import utc
from datetime import datetime
import time

def mainPage(request):
    page_posts = BlogPost.objects.all().order_by('-create_time')
    page_size = 5 #<page_size> posts in one page
    paginator = Paginator(page_posts,page_size)
    page_list = paginator.page_range
    page_num = page_list[len(page_list)-1]
    try:
    	page = int(request.GET.get('page','1'))
    except ValueError:
    	page = 1
    	print page
    try:
    	posts_page = paginator.page(page) #show the posts in the given page_num by GET
    except (EmptyPage, InvalidPage):
    	posts_page = paginator.page(paginator.num_pages)

    return render_to_response('index.html',{'page_posts':posts_page,'page_num':page_num,'page_list':page_list})

class archive_year:
    blogs_this_year = []
    this_year = 0
    def __init__(self,l,y):
    	self.blogs_this_year = l
    	self.this_year = y

def archivePage(request):
    list_by_year = []
    for i in range(2020,2010,-1): #temp 10 years
    	blogs_this_year = BlogPost.objects.filter(create_time__year=i).order_by('-create_time')
    	if len(blogs_this_year) != 0:
    	    list_this_year = archive_year(blogs_this_year,i)
    	    list_by_year.append(list_this_year)

    return render_to_response('archive.html',{'list_by_year':list_by_year})

def galleryPage(request):
    gallery_posts = GalleryPost.objects.all().order_by('-create_time')
    page_size = 5 #<page_size> posts in one page
    paginator = Paginator(gallery_posts,page_size)
    page_list = paginator.page_range
    page_num = page_list[len(page_list)-1]
    try:
    	page = int(request.GET.get('page','1'))
    except ValueError:
    	page = 1
    	print page

    try:
    	photos_page = paginator.page(page) #show the posts in the given page_num by GET
    except (EmptyPage, InvalidPage):
    	photos_page = paginator.page(paginator.num_pages)

    return render_to_response('gallery.html',{'page_photos':photos_page,'page_num':page_num,'page_list':page_list})

def aboutPage(request):
    client_ip = request.META['REMOTE_ADDR']
    city = get_city_by_ip(client_ip)
    return render_to_response('about.html',{'client_city':city})

def postPage(request):
    if request.method == 'GET':
	id = request.GET.get('id','');
	try:
	    blog = BlogPost.objects.get(id = id)
	    client_ip = request.META['REMOTE_ADDR']
	    try:
		visit_record = BlogVisit.objects.get(blog_id=id, visit_ip=client_ip)
            except BlogVisit.DoesNotExist: #never visit this blog
		new_visit_record = BlogVisit(blog=blog, visit_ip=client_ip, visit_time=datetime.now())
		new_visit_record.save()
		blog.counts = blog.counts + 1
		blog.save()
	    else: #has visited this blog
		record_sec = time.mktime(visit_record.visit_time.timetuple())
		now_sec = time.mktime(datetime.utcnow().replace(tzinfo=utc).timetuple()) #convert now time to utc
		#http://www.dannysite.com/blog/84/
		#http://segmentfault.com/q/1010000000405911
		period = now_sec - record_sec
		if(period > 86400): #over one day == 86400sec
		    blog.counts = blog.counts + 1
		    blog.save()
		#update visit time
		visit_record.visit_time = datetime.now()
		visit_record.save()
	    #city = get_city_by_ip(client_ip)
	except BlogPost.DoesNotExist:
	    raise Http404
	return render_to_response('post.html',{'blog':blog})
    else:
	raise Http404
