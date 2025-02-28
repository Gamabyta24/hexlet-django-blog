from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context={'app_name':'hexlet_django_blog'}
    return render(request, 'article/index.html',context=context)