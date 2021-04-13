from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Crud

# Create your views here.
def index(request):
    devicedata=Crud.objects.all()
    context={
        'devices':devicedata
    }
    return render(request,'crud/index.html',context)



def store(request):
    if request.method=='POST':
        # CATCH DATA
        model=request.POST.get('model')
        weight=request.POST.get('weight')
        price=request.POST.get('price')

        # INSERT DATA
        device=Crud()
        device.device_model = model
        device.device_weight = weight
        device.device_price = price
        device.save()
        return redirect('crud:index')
        # return render(request,'crud/test_data.html',{'device':device})
    return render(request,'crud/store.html')



def edit(request,id):
    device = Crud.objects.get(id=id)
    context={
        "device":device
    }
    return render(request,'crud/edit.html',context)



def update(request, id):
    device = Crud.objects.get(id=id)
    if request.method=='POST':
        # CATCH DATA
        model=request.POST.get('model')
        weight=request.POST.get('weight')
        price=request.POST.get('price')
        # UPDATE DATA
        device.device_model = model
        device.device_weight = weight
        device.device_price = price
        device.save()

        return redirect('crud:index')
    return HttpResponse(request,'crud:{{device.id}}/edit')


def delete(request,id):
    device =Crud.objects.get(id=id)
    device.delete()
    return redirect("../")