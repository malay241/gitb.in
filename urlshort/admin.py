from django.contrib import admin
from .models.urlshort import Urlshortadd
# Register your models here.
class AdminUrls(admin.ModelAdmin):
	list_display = ['original_url','shortend_url','keyword']



# Register your models here.
admin.site.register(Urlshortadd,AdminUrls)