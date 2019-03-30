  
from django.urls import include  , path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView , LogoutView , logout_then_login

from . import views


app_name = 'Users'
urlpatterns = [
    path('' , LoginView.as_view( template_name='users/login.html', ) , name = 'Login'),
    path('register/' , views.registration_view , name = 'register'),
    path('logout/' , login_required(LogoutView.as_view()) , name = 'logout'),
    path('<int:id>/edituser/' , views.editUser , name = 'edituser'),

    path('profile/order/' , login_required(views.order_view) , name = 'order'),
    path('profile/' , login_required(views.profile) , name = 'profile'),

    path('<int:id>/delete/' , login_required(views.delete) , name = 'delete'),
    path('profile/<int:id>/del/' , login_required(views.Pre_del.as_view()) , name = 'pre_delete'),
    path('profile/<int:id>/edit/' , login_required(views.edit) , name = 'edit'),
]
