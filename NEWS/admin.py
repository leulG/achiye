from django.contrib import admin
from .models import News

# Register your models here.

class PostNewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ['Title', {'fields' : ['Title']}],
        ['Sub Title', {'fields' : ['Sub_Title']}],
        ['Upload a video File Here If nesesory' , { 'fields' : ['Video']}],
        ['Upload a Image File Here If nesesory' , { 'fields' : ['Image']}],
        ['Write a description about the news here ' , { 'fields' : ['Description']}],
    ]    
    list_display = ['Title' ,  'Image' ,  'pub_date' ,  'modified']

    list_filter = ['Title' ,'Sub_Title' , 'Image' , 'pub_date' , 'modified']
admin.site.register(News , PostNewsAdmin)