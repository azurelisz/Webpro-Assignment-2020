from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return HttpResponse('<center><h1>This is dash board</h1></center>')