from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def january(request):
    return HttpResponse("This Works!")

def love(request):
    return HttpResponse("You are my world")

def django1(request):
    return HttpResponse("Learn Django more")