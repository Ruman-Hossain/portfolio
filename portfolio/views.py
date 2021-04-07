from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    text={
        'name':'Md Ruman Hossain',
        'age':25,
        'phone':'01723974489',
        'friend_name':['Mamun','Rahat','Shopnil','Mostafa','Pitom','Mridula']
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')