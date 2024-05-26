from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from blog.forms import SignUpForm

# Create your views here.
def index(request):
    context={"date": datetime.today()}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))

def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"article_{numero_article}.html", context={})
    return render(request, "article_not_found.html")

def signup(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci vous vous etes inscrits !!")
    else:
        form = SignUpForm()
        
    context = {
        "form" : form
    }
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(context, request))
    # return render(request, 'signup.html', context)