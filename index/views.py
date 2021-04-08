from django.http import HttpResponse
from django.shortcuts import render
from .models import about

def home(request):
    data=about.objects.all()[0]
    context={
        'about':data
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'contact.html')