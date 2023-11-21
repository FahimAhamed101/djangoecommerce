from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm,UpdateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form}
    return render(request,'register.html',context)
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    context = {'form' : form}
    return render(request,'login.html',context)
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')
@login_required(login_url='login')
def profile(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form' : form}
    return render(request,'profile.html',context)
@login_required(login_url='login')
def profiledelete(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request,'profiledelete.html')
