from django.shortcuts import redirect,render
from django.http import HttpResponse 

from django.contrib.auth.models import User,auth

from .forms import BookingForm

 
from .models import Departments,Docters,Booking


# Create your views here.

    

    
def explore(request):
    if 'username' in request.session:
        return render(request,'explore.html')
    else:
     return redirect('login')

    
    
def about(request):
     if 'username' in request.session:
     
      return render(request,'about.html')
     else:
         return redirect('login')
def Booking(request):
    if 'username' in request.session:
      
      if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
      else:

          form = BookingForm()
      
          dict_forms = {
             'form':form,

         }    
    
     
     
          return render(request,'booking.html',dict_forms)
    else:
        return redirect('login')

def docters(request):
    if 'username' in request.session:
       docters = Docters.objects.all()
       dict_docs={
        'docters':docters
      }
       return render(request,'docters.html',dict_docs)
    else:
        return redirect('login')
def contact(request):
    if 'username' in request.session:
        return render(request,'contact.html')
    else:
        return redirect('login')


    
    
def department(request):
    if 'username' in request.session:
        dict_dept={
        'dept':Departments.objects.all()
        }
        return render(request,'department.html',dict_dept)
    else:
        return redirect('login')

    