from django.shortcuts import render , get_object_or_404, redirect
from django.views import View , generic
from django.contrib.auth import (authenticate ,get_user_model ,login , logout )
# Create your views here.
from django.contrib.contenttypes.models import ContentType
from .models import JobOrder
from .forms import UserRegistration , UserJobOrder
from django.contrib import messages

def registration_view(request):
    if not request.user.is_authenticated:
        title = "Registration"
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            #login(request , user)
            return redirect('../')
        context = {
            'title' : title,
            'form' : form
        }
        return render(request , 'users/register.html' , context)
    return render(request , 'users/register.html' , context = {'err' : 'Forbidon attempt! sign out first'})

def order_view(request):
    title = 'Order A Job'
    inital_data = {
            'Title' : 'your title goes here',
            'Description' : 'your description'
        }
    form = UserJobOrder( request.POST or None , request.FILES or None ,initial=inital_data )
    if form.is_valid():

        title = form.cleaned_data.get('Title')
        File = form.cleaned_data.get('File')
        description = form.cleaned_data.get('Description')
        user = request.user
        new_job = JobOrder.objects.create(user = user , Title = title ,File = File , Description = description )
        new_job.save()
        messages.success(request  ,"sucsses",  extra_tags = 'html_safe')
        return redirect('../')
    context = {
        'title' : title,
        'form' : form
    }
    return render(request , 'users/order.html' , context)



def edit(request , id):
    title = 'Edit The Job'
    #instance = JobOrder.objects.get(id = id)
    instance = get_object_or_404(JobOrder , pk = id)
    if request.user == instance.user or request.user.is_superuser and instance.was_published_recently:
        form = UserJobOrder( request.POST or None , request.FILES or None , instance=instance)


        if form.is_valid():
            form.save()
            messages.success(request  ,"sucssesfuly changed.. ",  extra_tags = 'html_safe')
            return redirect('../../')
        context = {
            'title' : title,
            'form' : form
        }

        return render(request , 'users/order.html' , context)
    return render(request , 'users/order.html' , context = {'err' : 'Forbidon attempt'})
class Pre_del(View):
    def get(self , request  , id,  *args , **kwargs):
        obj = get_object_or_404(JobOrder , pk = id)
        if request.user == obj.user and obj.was_published_recently:

            context = {
                'Title' : 'are you sure you want to delete : ',
                'Obj' : obj
            }
            return render(request , 'users/pre_del.html' , context)
        return render(request , 'users/profile.html' , context = {'err' : 'Forbidon attempt'})


    

def delete(request , id):
    obj = get_object_or_404(JobOrder , pk = id)
    if request.user == obj.user or request.user.is_superuser and obj.was_published_recently and request.POST:


        if obj is not None:

            obj.delete()

            return redirect('/Users/profile')
        return render(request , 'users/profile.html' )
    return render(request , 'users/profile.html' , context = {'err' : 'Forbidon attempt'})


def profile(request):
    if request.user.is_authenticated:
        context = {}
        if request.user.is_superuser:
            u = get_user_model()
            user = u.objects.all()
            context['userr'] = user
            
        
        title = 'User Profile'
        orders = JobOrder.objects.order_by('-pub_date')
        context['title'] = title
        context['orders'] = orders
        return render(request , 'users/profile.html' , context)
    else:
        return render(request , 'users/profile.html' , context = {'err' : 'Forbidon attempt'})


def editUser(request , id):
    context = {}
    objs = []
    users = get_user_model()
    user = users.objects.get(pk = id)
    obj = JobOrder.objects.all()
    if user is not None:
        context['user'] = user
        for o in obj:
            if o.user == user:
                objs.append(o)
        context['objs'] = objs 
        return render(request , 'users/edituser.html' , context)

    return render(request , 'users/edituser.html' )



    