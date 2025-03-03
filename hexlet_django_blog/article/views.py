from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    context={'app_name':'hexlet_django_blog'}
    return render(request, 'article/index.html',context=context)

class IndexArticle(View):
    def get(self,request,tags,article_id,*args,**kwargs):
        context={'article_id':article_id,'tags':tags}
        return render(request, 'article/index.html',context=context)
    
class HomePageView(View):
    def get(self,request,*args,**kwargs):
        url = reverse('article',kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)