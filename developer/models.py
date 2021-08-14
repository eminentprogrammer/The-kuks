from django.db import models

class langauage(models.Model):
	name = models.CharField(max_length=200, unique=True)
	symbol = models.URLField(blank=True, default='')

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['name']

class tool(models.Model):
	name = models.CharField(max_length=200, unique=True,)
	symbol = models.URLField(blank=True, default='')
	def __str__(self):
		return str(self.name)
	class Meta:
		ordering = ['name']

class project(models.Model):
	image 		= models.ImageField(upload_to="projects/", default="project/default.png", blank=True, null=True)
	title 		= models.CharField(max_length=250)
	short_desc 	= models.TextField()
	completed 	= models.BooleanField(default=False)
	def __str__(self):
		return str(self.title)

class programmer(models.Model):
	username 	= models.CharField(max_length=200, unique=True)
	fullname 	= models.CharField(max_length=250)
	short_bio 	= models.TextField()
	dob 		= models.DateField(verbose_name="Date of Birth")
	github 		= models.CharField(max_length=200, help_text="Github username")
	projects 	= models.ManyToManyField(project, help_text="project", blank=True, null=True)
	lang 		= models.ManyToManyField(langauage, blank=True, null=True)
	tools 		= models.ManyToManyField(tool, blank=True, null=True)

	def __str__(self):
		return str(self.username)