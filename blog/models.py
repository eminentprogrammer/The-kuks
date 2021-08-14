from django.db import models
from django.urls import reverse
from django.utils.text import slugify

def upload_location(instance, filename):
	path = 'blog/{}/{}'.format(str(instance.tag), str(filename))
	return path

class tag(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('tag', args=[str(self.name)])
	class Meta:
		verbose_name_plural = "Tags"
		ordering =  ['name', 'id']


class Entry(models.Model):
	image 		= models.ImageField(upload_to=upload_location, blank=True, null=True, default="image/default.png")
	title 		= models.CharField(max_length=250, help_text="Blog title", unique=True)
	body		= models.TextField()
	youtube_src = models.CharField(max_length=200, default='', blank=True)
	tag 		= models.ForeignKey(tag, on_delete=models.CASCADE, related_name="tags", null=True, default=1)
	pub_date 	= models.DateField(auto_now_add=True)
	slug 		= models.SlugField(blank=True, default='')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Entry, self).save()

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.slug)])

	class Meta:
		verbose_name_plural = "Blog Entry."
		ordering = ['-pub_date','-id']
