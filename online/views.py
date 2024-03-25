from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def add_author(request):
    if request.method=='POST':
        author_name=request.POST.get('name')
        author_email=request.POST.get('email')
        author_phone=request.POST.get('phone')
        image=''
        if request.FILES:
            image=request.FILES['image']
        Author.objects.create(name=author_name,email=author_email,phone=author_phone,image=image)
        back=request.META.get('HTTP_REFERER')
        messages.success(request,'Author added succsfully')
        return redirect(back)
        
    else:
        return render(request,'add_author.html')
    
def show_author(request):
    data={
        'authors':Author.objects.all()
        }
   
    return render(request,'show_author.html',data) 

def add_category(request):
    if request.method=='POST':
       category_name=request.POST.get('name')
       Category.objects.create(name=category_name)
       back=request.META.get('HTTP_REFERER')
       messages.success(request,'category added succsfully')
       return redirect(back)
       
    else:
        data={
            'categoryData': Category.objects.all()
            
        }
        return render(request, 'add_category.html',data)