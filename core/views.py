from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from .forms import rcf
from .models import Course, Typee, rc, Profile, Message
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

# Create your views here.
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'name':user.profile.name,'csem':user.profile.csem,})

def landing(request):
    return render(request,'core/landing.html')

def loginn(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')    

    context={}
    return render(request, 'core/login.html', context)

def signup(request):
    form=SignUpForm(request.POST)
    if request.method=='POST':
        #print("chackpoint1")
        form=SignUpForm(request.POST)
        print(form.errors)
        #print("chackpoint2")
        user=form.save()
      
        user.refresh_from_db()
        user.profile.name = form.cleaned_data.get('name')
        update_user_data(user) 
       
        user.profile.csem = form.cleaned_data.get('csem')
        update_user_data(user) 

        user.save()
        raw_password = form.cleaned_data.get('password1')
        user=authenticate(username=user.username, password=raw_password)
        login(request,user)
        
        return redirect('home')
    return render(request,'core/signup.html',{'form':form})

@login_required(login_url='login')
def upload(request):
    topics = Course.objects.all()
    topics2 = Typee.objects.all()
    if request.method == 'POST':
        print("kk")
        form = rcf(request.POST, request.FILES)
        global Rc
        print(form.errors)
        #if form.is_valid():
            #print("kkkk")
        Rc=rc()
        Rc.poster=request.user
        Rc.sem=form.cleaned_data['sem']

        cc=form.data['course']
        tc,waste = Course.objects.get_or_create(cname=cc)
        Rc.course=tc

        cc2=form.data['typee']
        tc2,waste2 = Typee.objects.get_or_create(tname=cc2)
        Rc.typee=tc2

        Rc.title=form.cleaned_data['title']
        Rc.pdf=form.cleaned_data['pdf']
        Rc.dis=form.cleaned_data['dis']
        Rc.save()
        return redirect('landing')
    else:
        form = rcf()

    return render(request, 'core/upload.html', {
        'form': form,
        'topics': topics,
        'topics2': topics2

    })

@login_required(login_url='login')
def clist(request):
    q=request.user.profile.csem
    cs=Course.objects.filter(sem=q)
    context={
        'User':request.user,
        'cs':cs
    }
    return render(request,'core/clist.html',context)

@login_required(login_url='login')
def tlist(request, pk):
    
    coursee = Course.objects.get(cname=pk)
    ts=Typee.objects.all()
    context = {'course': coursee,'ts':ts}
    return render(request, 'core/tlist.html', context)

@login_required(login_url='login')
def lisst(request,pk,pkk):
    coursee = Course.objects.get(cname=pk)
    ts= Typee.objects.get(tname=pkk)
    rcs=rc.objects.filter(typee=ts)
    context = {'course': coursee,'ts':ts,'rcs':rcs}
    return render(request, 'core/lisst.html', context)

@login_required(login_url='login')
def info(request, pk):
    rcs = rc.objects.get(id=pk)
    mess = Message.objects.filter(rrc=rcs)
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            rrc=rcs,
            body=request.POST.get('body')
        )
        return redirect('info', pk=rcs.id)
    
    
    context = {'rc':rcs,'mess':mess}
    return render(request, 'core/info.html', context)

@login_required(login_url='login')
def semc(request,pk):
    p=request.user.profile
    p.csem=pk
    p.save()
    return redirect('clist')

@login_required(login_url='login')
def home(request):
    q=request.user.profile.csem
    context={
        'User':request.user
    }
    return render(request,'core/home.html',context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('landing')