from django.contrib import admin
from django.urls import include  , path
from . import views




app_name = 'Home'
urlpatterns = [
    path('' , views.home , name = 'home'),
  
]