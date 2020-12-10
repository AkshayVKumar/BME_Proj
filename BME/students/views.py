from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"students/index.html")

def aboutus(request):
    return render(request,"students/aboutus.html")

def contact_us(request):
    return render(request,"students/contactus.html")
