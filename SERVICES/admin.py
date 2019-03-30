from django.contrib import admin
from .models import Service
# Register your models here.
class AddServicesAdmin(admin.ModelAdmin):
    fieldsets = [
        ['Title', {'fields' : ['Title']}],
        ['Sub Title', {'fields' : ['Sub_Title']}],
        ['Description....', {'fields' : ['Description']}],
        
    ]
    list_display = ['Title' ,  'pub_date' , 'modified']

    list_filter = ['Title' , 'pub_date' , 'modified']
     

admin.site.register(Service , AddServicesAdmin)