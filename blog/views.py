from . models import *
from . forms import BlogEntry, UpdateBlogForm 
from django.shortcuts import render, redirect, get_object_or_404
from .utils import paginateblog
import json
from developer.models import programmer, langauage, tool

def homepage(request):
	blog = []
	custom_range, blog, paginator = paginateblog(request,blog, 5)
	return render(request, 'blog/index.html', context={'blog':blog})

def create(request):
	form = BlogEntry()
	value = tag.objects.all()
	if request.method == 'POST':
		form = BlogEntry(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			instance = get_object_or_404(Entry, title=str(instance.title))		
			return redirect('detail', instance.slug)
		redirect('create-blog')
	return render(request, 'blog/create-blog.html', context={'CreateBlogForm':form, 'tag':value})

def detail(request, slug):
	blog = get_object_or_404(Entry, slug=slug)
	return render(request, 'blog/detail.html', context={'blog':blog})

def edit(request, slug):
	context = {}
	blog = Entry.objects.get(slug=slug)
	value = tag.objects.all()
	
	if request.POST:
		form = UpdateBlogForm(request.POST or None, request.FILES or None, instance=blog)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('detail', slug=instance.slug)

	form = UpdateBlogForm(
		initial = {
				"title"	: blog.title,
				"body"	: blog.body,
				"tag"	: blog.tag,
				"slug"	: blog.slug,
				"image"	: blog.image,
		}

	)

	return render(request, 'blog/edit.html', context={'form':form, 'tag':value})

def about(request):
	user = get_object_or_404(programmer, username="Igwesi")
	lang = langauage.objects.all()
	tools = tool.objects.all() 
	return render(request, 'about.html', context={'user':user, 'lang':lang,'tools':tools})
