from . models import *
from . forms import BlogEntry, UpdateBlogForm 
from django.shortcuts import render, redirect, get_object_or_404
from .utils import paginateblog

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

def detail(request, slug=None):
	blog = get_object_or_404(Entry, slug=slug)
	return render(request, 'blog/detail.html', context={'blog':blog})


def edit(request, slug=None):
	context = {}
	blog_post = get_object_or_404(Entry, slug=slug)
	value = tag.objects.all()
	if request.method == "POST":
		form = UpdateBlogForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj
	form = UpdateBlogForm(
		initial = {
				"title": blog_post.title,
				"body": blog_post.body,
				"tag": blog_post.tag,
				"slug": blog_post.slug,
		}
		)
	if blog_post.image:
		form.initial["image"]: blog_post.image
	return render(request, 'blog/edit.html', context={'form':form, 'tag':value})