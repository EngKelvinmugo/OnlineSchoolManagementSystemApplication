
# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .forms import *
 
def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()
 
    context = {
        'notice':notice,
        'marks':marks,
        'attendance':attendance,
    }
    return render(request,'app/home.html',context)
 
def addAttendance(request):    
    if request.user.is_authenticated:
        form=addAttendanceform()
        if(request.method=='POST'):
            form=addAttendanceform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addAttendance.html',context)
    else: 
        return redirect('home')
 
def addMarks(request): 
    if request.user.is_authenticated:
        form=addMarksform()
        if(request.method=='POST'):
            form=addMarksform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addMarks.html',context)
    else: 
        return redirect('home')  
 
def addNotice(request):    
    if request.user.is_authenticated:
        form=addNoticeform()
        if(request.method=='POST'):
            form=addNoticeform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addNotice.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'app/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'app/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')
