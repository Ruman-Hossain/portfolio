from django.http import HttpResponse
from django.shortcuts import render

def employee(request):
    return HttpResponse("This is Our Employee Module Home Page")

def profile(request):
    return render(request,'employee/profile.html')