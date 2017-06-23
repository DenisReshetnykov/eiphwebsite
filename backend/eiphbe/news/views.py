from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Good News, Everyone!")

def detail(request, news_id):
    return HttpResponse("News # %s." % news_id)

# Create your views here.
