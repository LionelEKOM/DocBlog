from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.views import View
from requests import request
from blogModels.forms import BlogPostForm
from blogModels.models import BlogPost

# Create your views here.
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

class HomeView(TemplateView):
    title = ""
    template_name = "home.html"
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse(f'GET request!, {self.title}')

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Club d'elite"
        return context
    
class BlogIndexView(ListView):
    model = BlogPost
    context_object_name = 'Blogs'
    template_name='blog-list.html'
    
class BlogDetailView(DetailView):
    model = BlogPost
    template_name='blogdetail.html'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blogform.html"
    success_url = reverse_lazy("blog-list")
    # fields = [
    #         "title",
    #         "content",
    #     ]
    form_class = BlogPostForm
    
    # def get_success_url(self):
    #     return reverse("blog-list")
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.published = True
        return super().form_valid(form)
    


def creat(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid:
            if request.user.is_authenticated:
                form.instance.author = request.user
            form.save()
            # return HttpResponseRedirect(request.path)
            return HttpResponseRedirect(reverse('blog-list'))
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        
        init_values["date"] = datetime.today()
        init_values["title"] = "Hisense the best brand tv"
        form = BlogPostForm(initial=init_values)
        
    context = {
        "form": form
    }
    template = loader.get_template('article.html')
    return HttpResponse(template.render(context, request))