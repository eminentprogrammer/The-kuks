from django.forms import ModelForm
from . models import Entry


class BlogEntry(ModelForm):

	class Meta:
		model = Entry
		fields = ['image','title','tag','body']


class UpdateBlogForm(ModelForm):

	class Meta:
		model = Entry
		fields = ['image','title','tag','body', 'slug']

	def save(self, commit=True):
		blog_post = self.instance
		blog_post.title = self.cleaned_data['title']
		blog_post.body = self.cleaned_data['body']
		blog_post.tag = self.cleaned_data['tag']
		blog_post.slug = self.cleaned_data['slug']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']

		if commit:
			blog_post.save()
		return blog_post
