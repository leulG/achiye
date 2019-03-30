from django.shortcuts import render , get_object_or_404
from django.http import Http404
from .models import Service
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import View

# Create your views here.
def index(request):
    services = Service.objects.order_by('-pub_date')[:10]
    paginator = Paginator(services , 6) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        service = paginator.get_page(page)
    except PageNotAnInteger:
        service = paginator.get_page(1)
    except EmptyPage:
        service = paginator.get_page(paginator.num_pages)
    context = {
        'Title' : 'Lists Of Services We Offer',
        'services' : service
    }
    return render(request , 'SERVICES/index.html' , context)
def detail(request , id):
    model = Service
    #service = get_object_or_404(model , id = id)
    try:
        service = Service.objects.get(id = id)
    except:
        raise Http404
    context = {
        'service' : service
    }

    return render(request , 'SERVICES/detail.html' , context)
class Search(View):
    
    template_name = 'SERVICES/search.html'
    
    objects = Service.objects.all()
    
    
    def post(self , request , *args , **kwargs):
        
        context = {}
        dictionary = [] #initializing the dictionary
        for obj in self.objects:
            if request.POST['Title'] == obj.Title: #cheking if the title matches
                dictionary.append(obj) #pushing it in the dictionary
        if len(dictionary) == 0: #checking if no matches has been found
           return render(request , 'SERVICES/search.html' ,{
               'err': 'no data with specific value'
        }) 
        context['objects'] = dictionary #puting the dictionary in the context to serve the front
        
        return render(request , self.template_name ,context)



    