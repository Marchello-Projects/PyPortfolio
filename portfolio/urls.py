from django.shortcuts import redirect
from django.urls import path
from . import views

def root_redirect(request):
    return redirect('login')

urlpatterns = [
    path('', root_redirect),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('editor/', views.editor_view, name='editor')
]