from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'popa'
        return context
    


def index(request):
    return render(request, 'index.html',context={'who':'world'})
def about(request):
    return render(request, 'about.html')