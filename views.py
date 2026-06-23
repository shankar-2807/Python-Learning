from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def demo1(request):
    return render(request,"addNumbers.html")

def showResult(request):
    first = int(request.GET["first"])
    second = int(request.GET["second"])
    sum = first+second
    return HttpResponse(sum)

def addProduct(request):
    return render(request,"addProduct.html")

def saveProduct(request):
    pname = request.GET["pname"]
    price = request.GET["price"]
    qty = request.GET["qty"]
    p1 = Product(pname=pname,price=price,qty=qty)
    p1.save()
    return HttpResponse(str(p1.id)+" Added")


def showAllProducts(request):
    prds = Product.objects.all()
    return render(request,"ShowAllProducts.html",{"prds":prds})

def updateProduct(request):
    pid = request.GET["prd_id"]
    qty = request.GET["qty"]
    prd = Product.objects.get(id = pid)
    prd.qty = qty
    prd.save()
    return HttpResponse("Done")


