from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from .forms import movieForm
# Create your views here.


def demo(request):
    movie=movies.objects.all()

    context={
        'movielist':movie
    }
    return render(request,'index.html',context)


def movdetails(request,id):
    movie = movies.objects.filter(id=id)


    return render(request,'details.html',{'name':movie})

def add_details(request):
    if request.method=='POST':
        name=request.POST.get('name')
        img = request.FILES['img']
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        alldata=movies(name=name,img=img,desc=desc,year=year)
        alldata.save()


    return render(request,'add.html')

def update(request,id):
    mov=movies.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj1':mov,'form':form})


def delete(request,id):
    if request.method == 'POST':
        movi=movies.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')



