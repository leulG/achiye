from django.shortcuts import render
from .models import Document , Type_Choices
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    latest_Document_list = Document.objects.order_by('-pub_date')
    paginator = Paginator(latest_Document_list , 6) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        latest_Document= paginator.get_page(page)
    except PageNotAnInteger:
        latest_Document = paginator.get_page(1)
    except EmptyPage:
        latest_Document = paginator.get_page(paginator.num_pages)
 

        
    context = {
        'Title' : 'Pdf Files To Download',
        'latest_Docs' : latest_Document
    }
    return render(request , 'DOCS/index.html' , context)
def detail(request , id):
    Doc = Document.objects.get(id = id)
    context = {
        'Title' : 'Pdf Files To Download',
        'Doc' : Doc
    }
    return render(request , 'DOCS/detail.html' , context)


class Search(View):
    
    template_name = 'DOCS/search.html'
    objects = Document.objects.all()
    
    
    
    def post(self , request , *args , **kwargs):
        context = {}
        dictionary = [] #initializing the dictionary
        for obj in self.objects:
            if request.POST['Title'] in obj.Title: #cheking if the title matches
                dictionary.append(obj) #pushing it in the dictionary
        if len(dictionary) == 0: #checking if no matches has been found
           return render(request , 'DOCS/search.html' ,{
               'err': 'no data with specific value'
        }) 
        context['objects'] = dictionary #puting the dictionary in the context to serve the front
        
        return render(request , self.template_name ,context)


