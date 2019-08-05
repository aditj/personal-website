from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Project,Article,Interest,Book,Contact
# Create your views here.
def index(request):

    projects=Project.objects.all()
    articles=Article.objects.all()
    interests=Interest.objects.all()
    books=Book.objects.all()
    context={'projects':projects,'articles':articles,'interest':interests,'books':books}
    return render(request,'index/index.html',context)
def article(request,article_id):
    return HttpResponse("Hello")
def list(request,type):
    return HttpResponse("Hello")
def contact(request):
    if request.method=="POST":
        a=Contact(request.POST.get("name"),request.POST.get("email"),request.POST.get("phone"),request.POST.get("message"))
        a.save()
        return HttpResponseRedirect('/index',{'message':"Submitted"})
