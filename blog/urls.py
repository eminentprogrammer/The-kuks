from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('create-blog', views.create, name="create-blog"),
	path('blog/<slug:slug>', views.detail, name="detail"),
	path('blog/<slug:slug>/edit', views.edit, name="edit-blog"),
	path('about', views.about, name='about')
]
