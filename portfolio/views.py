from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.files.base import ContentFile
from .forms import UserLoginForm, UserRegisterForm, CvForm
from .models import CvFile
from .utils import generate_cv_docx

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

@login_required
def editor_view(request):
    if request.method == 'POST':
        form = CvForm(request.POST)

        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            form.save_m2m()

            doc_buffer = generate_cv_docx(cv)
            filename = f'cv_{request.user.username}_{cv.id}.docx'

            CvFile.objects.create(
                user=request.user,
                cv=cv,
                file=ContentFile(doc_buffer.read(), name=filename)
            )

            return redirect('editor')  

    else:
        form = CvForm()

    return render(request, 'portfolio/editor.html', {'form': form})