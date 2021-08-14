from django.forms import ModelForm
from . models import Entry


class BlogEntry(ModelForm):

	class Meta:
		model = Entry
		fields = ['image','title','youtube_src','body','tag']


class UpdateBlogForm(ModelForm):

	class Meta:
		model = Entry
		fields = ['image','title','body', 'tag','slug']
