from django.shortcuts import render
from .models import Message
from .forms import MessageForm 
from django.contrib.auth import (authenticate ,get_user_model ,login , logout )
# Create your views here.
from django.views import View

from django.contrib.auth.decorators import login_required


class index(View):
    template_name = 'Message/message.html'
    _user = get_user_model()
    context = {}
    def get(self ,request ,id = None, *args , **kwargs):
        if id is not None:
            user = self._user.objects.get(id = id)
            self.context['user'] = user
            messages = Message.objects.filter(user = user)
            self.context['messages'] = messages 
            return render(request ,  self.template_name, self.context)


        if request.user.is_superuser:
            users = self._user.objects.all()
            self.context['users'] = users
            return render(request ,  self.template_name, self.context)
        
        form = MessageForm()
        self.context['form'] = form
        return render(request ,  self.template_name, self.context)
    
    def post(self ,request, *args , **kwargs):
        form = MessageForm(request.POST or None)
        context = {
            'form' : form
        }
        if form.is_valid():
            user = request.user
            message = form.cleaned_data.get('message')
            newMessage = Message.objects.create(user = user , message = message)
            newMessage.save()
        return render(request ,  self.template_name, context)

    

    
    