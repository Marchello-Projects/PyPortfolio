from django import forms
from django.contrib.auth.models import User
from .models import Cv
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.utils import ErrorList

class SilentErrorList(ErrorList):
    def __str__(self):
        return ""
    def as_ul(self):
        return ""
    def as_text(self):
        return ""
    def as_json(self, escape_html=False):
        return ""

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        kwargs['error_class'] = SilentErrorList
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs['error_class'] = SilentErrorList
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class CvForm(forms.Form):
    class Meta:
        model = Cv
        exclude = ('user',)