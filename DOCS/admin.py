from django.contrib import admin

# Register your models here.
from .models import Document
class PostDocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        ['Enter a Title Here', {'fields' : ['Title']}],
        ['Upload a pdf File Here' , { 'fields' : ['File']}],
        ['Select a Type and add a description befor u save', {'fields' : ['Type' , 'Description']}],
       # ['Description abot the document', {'fields' : ['Description']}],
        
    ]
    list_display = ['Title' , 'File' , 'pub_date' , 'Type']

    list_filter = ['Title' , 'pub_date']


     

admin.site.register(Document , PostDocumentAdmin)