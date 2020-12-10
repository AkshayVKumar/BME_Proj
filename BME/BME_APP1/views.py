from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"bme_app1/index.html")

def aboutus(request):
    return render(request,"bme_app1/aboutus.html")

def contact_us(request):
    return render(request,"bme_app1/contactus.html")
