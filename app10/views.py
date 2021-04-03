from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("<h1> Welcom to index app10</h1>")

def sample10(request):
    return render(request,"app10/sample10.html")