from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import addpro

# Create your views here.


def saveimg(request): 
  
    if request.method == 'POST': 
        form = addpro(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = addpro() 
    return render(request, 'testapp/add.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 