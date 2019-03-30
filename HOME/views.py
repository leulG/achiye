from django.shortcuts import render
from NEWS.models import News
from DOCS.models import Document
from SERVICES.models import Service

# Create your views here.

def home(request):
    array = ['fa-heart' , 'fa-code' , 'fa-paper-plane' , 'fa-gem']
    services = Service.objects.order_by('-pub_date')[:4]
    Newss = News.objects.order_by('-pub_date')[:6]
    
    context = {
        'services' : services,
        'Newss': Newss,
        'arr' : array
      
    }

    return render(request , 'HOME/index.html'  ,context)
    
    