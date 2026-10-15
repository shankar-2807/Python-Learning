from django.shortcuts import render
from django.http import HttpResponse

def helloFromFirst(request):
    return HttpResponse('Hello from First App')

def demoHtml(request):
    return render(request="demo.html")

def login(request):
    if request.method == "GET":
        return render (request,"login.html")
    else:
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")

        if uname == "Shankar" and pwd == "admin@123":
            return HttpResponse("Login Successful")
        else:
            return HttpResponse("Login Failed")
        

