from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import AdminLoginForm, UpdateForm
from home.models import Booking, Docters


# Create your views here.
def adminlogin(request):
    if 'username' in request.session:
        return redirect('adminhome')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)


        if user is not None:
            if user.is_superuser:
                request.session['username'] = username
                auth.login(request,user)
                print('admin loggined')
                return redirect('adminhome')

              
            else:
                return redirect('adminlogin')
            
            
            
           
        else:
            return redirect('adminlogin')
    else:
        form = AdminLoginForm()
        dict_forms = {
           'form':form
        }
            
    
        return render(request,'adminlogin.html',dict_forms) 
def adminhome(request):
    if 'username' in request.session:
        seb = User.objects.all() 
        booking = Booking.objects.all()
        docters = Docters.objects.all()
        dict_obj ={
        'seb':seb ,
        'booking':booking,
        'docters':docters
        }
        return render(request,'adminhome.html',dict_obj)
    else:
        return redirect('login')

    """seb = User.objects.all() 
    dict_obj ={
        'seb':seb    
     }"""
    return render (request,'adminhome.html',dict_obj)
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('adminhome')
    
def update_data(request,id):
    if request.method == 'POST':
        pi =User.objects.get(pk=id)
        ann = UpdateForm(request.POST,instance=pi)
        if ann.is_valid():
          ann.save()
          return redirect('adminhome')
    else:
        pi = User.objects.get(pk=id)
        ann = UpdateForm(instance=pi)

    return render(request,'updatedata.html',{'form':ann,'id':id})
def adminlogout(request):
    if 'username' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect('adminlogin')

