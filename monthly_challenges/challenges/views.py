from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("This works! 1th Month")

def february(request):
    return HttpResponse("2th Month")