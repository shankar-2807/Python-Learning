from django.shortcuts import render
from django.http import HttpResponse

def helloFromMyApp2(request):
    return HttpResponse('Hello from MyApp2')
# Create your views here.

