from django.http import HttpResponse
from django.shortcuts import render
from .models import about,slider

def home(request):
    aboutdata=about.objects.all()[0]
    sliderdata=slider.objects.all()
    context={
        'about':aboutdata,
        'slider':sliderdata
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'contact.html')