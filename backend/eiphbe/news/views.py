from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Good News, Everyone!")

# Create your views here.
