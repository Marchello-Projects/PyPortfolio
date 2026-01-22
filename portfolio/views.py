from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('editor')
    else:
        form = UserLoginForm()

    return render(request, 'portfolio/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            return redirect('login') 
    else:
        form = UserRegisterForm()
    
    return render(request, 'portfolio/register.html', {'form': form})

def editor_view(request):
    return render(request, 'portfolio/editor.html')