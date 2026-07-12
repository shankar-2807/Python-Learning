from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Welcome to Django development')

def demo(request):
    return render(request="demo.html")

# def login(request):
#     if request.method == "GET":
#         return render (request,"login.html")
#     else:
#         uname = request.POST.get("uname")
#         pwd = request.POST.get("pwd")

#         if uname == "Firstbit" and pwd == "admin@123":
#             return HttpResponse("Login Successful")
#         else:
#             return HttpResponse("Login Failed")
        
# def demo(requet):
#     return render(requet,"demo.html")
        

def displayName(request):
    fname = "Vaishali"
    lname = "Reddy"
    return render(request,"displayName.html",
                  {"fname":fname,"lname":lname})

def displayList(request):
    data = ['Prashant' , 'Gopi', 'Krish', 'Hemant', 'Reema']
    return render(request,"displayList.html",
                  {"data":data})

def displayDict(request):
    data = {101:"Prashant", 102:"Gopi", 103:"Krish", 104:"Hemant", 105:"Heema"}
    return render(request,"displayDict.html",{"data":data})

def displayStudent(request):
    data = {101:["Prashant",23,77],
            102:["Gopi",24,76] ,
            103:["Krish",25,67],
            104:["Hemant",21,71],
            105:["Heema",22,68]}
    return render(request,"displayDict.html",{"data":data})

