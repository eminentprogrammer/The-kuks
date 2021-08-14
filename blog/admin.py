from django.contrib import admin
from . models import *
from django.utils.html import format_html

@admin.register(Entry) 
class EntryAdmin(admin.ModelAdmin):
    def page(self, obj):
        return format_html('<body style="background:green"></body>')

    def image_tag(self, obj):
        return format_html('<img style="height:50px; width:70px" src="{}"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
    def tag_tag(self, obj):
    	return format_html('<p style="color:blue">{}</p>'.format(obj.tag))

    list_display = ['title','youtube_src','tag_tag','image_tag','pub_date', 'page']

admin.site.register(tag)