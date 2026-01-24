from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str
from .forms import UserLoginForm, UserRegisterForm, CvForm
from .models import CvFile
from .utils import generate_cv_docx

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_staff:
                return redirect('admin:index')

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

@login_required
def history_view(request):
    files = CvFile.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'portfolio/history.html', {
        'files': files
    })

@login_required
def download_cv(request, pk):
    cv_file = get_object_or_404(CvFile, pk=pk, user=request.user)

    response = HttpResponse(
        cv_file.file.open('rb'),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="{smart_str(cv_file.filename)}"'
    )
    return response

@login_required
def delete_cv(request, pk):
    cv_file = get_object_or_404(CvFile, pk=pk, user=request.user)

    if request.method == 'POST':
        cv_file.delete()
        return redirect('history')

    return redirect('history')