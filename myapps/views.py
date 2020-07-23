from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"myapps/sample.html",{'name':"saif",'add':"lakhimpur"})
def index2(request):
    return HttpResponse("<h1>hello friends chaii Pi lo</h1>")
def index3(request,n):
    return HttpResponse("{}".format(n))    