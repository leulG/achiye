from django.contrib import admin
from django.urls import include  , path


from . import views


app_name = 'News'
urlpatterns = [
    path('' , views.index.as_view() , name = 'index'),
    path('<int:id>/detail/' , views.detail , name = 'detail'),
    path('search/' , views.Search.as_view() , name = 'search'),
  
]