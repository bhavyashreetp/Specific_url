from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>virat is a good batsman</h1>')

def maxwell(request):
    return HttpResponse('<h1>maxwell is one of the fastest scorers in world cricket</h1>')