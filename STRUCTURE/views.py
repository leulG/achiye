from django.shortcuts import render
from .models import Structure
# Create your views here.
def index(request):
    structures = Structure.objects.all()
    context = {
        'structures' : structures
    }
    return render(request , 'STRUCTURE/index.html' , context)