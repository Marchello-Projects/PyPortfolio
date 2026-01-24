from django.shortcuts import redirect
from django.urls import path

from . import views


def root_redirect(request):
    return redirect("login")


urlpatterns = [
    path("", root_redirect),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("editor/", views.editor_view, name="editor"),
    path("history/", views.history_view, name="history"),
    path("cv/<int:pk>/download/", views.download_cv, name="cv_download"),
    path("cv/<int:pk>/delete/", views.delete_cv, name="cv_delete"),
]
