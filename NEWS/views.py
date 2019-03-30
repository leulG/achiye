from django.shortcuts import render , get_object_or_404 
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


from .models import News
# Create your views here.
'''def index(request):
   latest_News_list = News.objects.order_by('-pub_date')[:10] 
   
   context = {
       'Title' : 'News',
       'latest_News_list' : latest_News_list
   }
   return render(request , 'NEWS/index.html' , context)'''



class index(View):
    template_name = 'NEWS/index.html'
    def get(self , request , *args , **kwargs):
        latest_News_list = News.objects.order_by('-pub_date') 
        paginator = Paginator(latest_News_list , 6) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            latest_News = paginator.get_page(page)
        except PageNotAnInteger:
            latest_News = paginator.get_page(1)
        except EmptyPage:
            latest_News = paginator.get_page(paginator.num_pages)
        
        context = {
            'Title' : 'News',
            'latest_News' : latest_News
        }
        return render(request , 'NEWS/index.html' , context)


class Search(View):
    login_required = True
    template_name = 'NEWS/search.html'
    objects =  News.objects.all()
    
    
    
    def post(self , request , *args , **kwargs):
        context = {}
        dictionary = [] #initializing the dictionary
        for obj in self.objects:
            if request.POST['Title'] in obj.Title: #cheking if the title matches
                dictionary.append(obj) #pushing it in the dictionary
        if len(dictionary) == 0: #checking if no matches has been found
           return render(request , 'NEWS/search.html' ,{
               'err': 'no data with specific value'
        }) 
        context['objects'] = dictionary #puting the dictionary in the context to serve the front
        
        return render(request , self.template_name ,context)





def detail(request , id):
    model = News
    news = get_object_or_404(model , id = id)
    context = {
       'Title' : 'News',
       'news' : news
    }
    return render(request , 'NEWS/detail.html' , context)