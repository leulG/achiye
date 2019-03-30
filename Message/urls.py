  
from django.urls import include  , path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView , LogoutView , logout_then_login
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'message'
urlpatterns = [
    path('' , login_required(views.index.as_view()) , name = 'index' ),
    path('<int:id>' , login_required(views.index.as_view()) , name = 'detail' )
]