from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def yash(request):
    return HttpResponse('<h1>yash is an pan India star</h1>')

def kicha(request):
    return HttpResponse('<h1>kicha is a best actor</h1>')
