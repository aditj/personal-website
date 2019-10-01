from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Project,Article,Interest,Book,Contact
from django.views.decorators.csrf import csrf_exempt

import git
# Create your views here.
def index(request):

    projects=Project.objects.all().order_by('done_on').reverse()[0:3]
    articles=Article.objects.all()
    interests=Interest.objects.all()
    books=Book.objects.all()
    context={'projects':projects,'articles':articles,'interest':interests,'books':books}
    return render(request,'index/index.html',context)
def article(request,article_id):
    return HttpResponse("Hello")
def list(request,type):
    return HttpResponse("Hello")
def submit(request):
    if request.method=="POST":
        a=Contact(request.POST.get("name"),request.POST.get("email"),request.POST.get("phone"),request.POST.get("message"))
        a.save()
        return HttpResponseRedirect('/index',{'message':"Submitted"})


@csrf_exempt
def webhook(request):
  if request.method == 'POST':
    repo = git.Repo('/home/aditjain/personal-website')
    
    origin = repo.remotes.origin
    origin.pull()
    return HttpResponse("Success")
  else:
    return HttpResponse("Cool")
