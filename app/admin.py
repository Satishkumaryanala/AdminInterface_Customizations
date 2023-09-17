from django.contrib import admin
from app.models import *
# Register your models here.

class CustomWeb(admin.ModelAdmin):
    list_display = ['topic_name','name','url']
    list_display_links = ('name',)
    list_editable = ['url']
    list_per_page = 2
    search_fields = ['name']
    list_filter = ['topic_name']

class CustomTopic(admin.ModelAdmin):
    list_display = ['topic_name']
    list_display_links = ('topic_name',)
    # list_editable = ['url']
    list_per_page = 2
    search_fields = ['topic_name']
    list_filter = ['topic_name']

class CustomAR(admin.ModelAdmin):
    list_display = ['date','name','email','author']
    list_display_links = ('date',)
    list_editable = ['author']
    list_per_page = 2
    search_fields = ['name']
    list_filter = ['email']

admin.site.register(Topic,CustomTopic)

admin.site.register(webpage,CustomWeb)

admin.site.register(AccessRecord,CustomAR)