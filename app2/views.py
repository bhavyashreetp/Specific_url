from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def yash(request):
    return HttpResponse('<h1>yash is a pan India star</h1>')

def kiccha(request):
    return HttpResponse('<h1>kiccha is a best actor</h1>')
