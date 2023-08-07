from django.shortcuts import redirect,render
from django.http import HttpResponse

from .forms import BookingForm,LoginForm


from .models import Departments,Docters


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
   
    return render(request,'login.html')
def explore(request):
    
    return render(request,'explore.html')
def about(request):
     return render(request,'about.html')
def Booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_forms = {
        'form':form
    }
    return render(request,'booking.html',dict_forms)
def docters(request):
    dict_docs={
        'docters':Docters.objects.all()
    }
    return render(request,'docters.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)