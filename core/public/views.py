from django.shortcuts import render
from .models import *

# Create your views here.

def index (request):

    Hero_banner = IndexObjects.objects.all()
    context = {
        'hero_banner' : Hero_banner
    }
    return render (request, 'public/pages/index-3.html', context=context)