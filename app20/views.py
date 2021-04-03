from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("<h1> Welcom to index of app20</h1>")

def sample20(request):
    return render(request,"app20/sample20.html")