
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include  , path
from . import views
app_name = 'Docs'
urlpatterns = [
    path('' ,  login_required(views.index) , name = 'index'),
    path('<int:id>/detail' ,  login_required(views.detail) , name = 'detail'),
    path('search/' ,  login_required(views.Search.as_view()) , name = 'search'),
  
]