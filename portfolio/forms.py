from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList

from .models import Cv


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
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        kwargs["error_class"] = SilentErrorList
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs["error_class"] = SilentErrorList
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )


class CvForm(forms.ModelForm):
    summary = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "class": "my-input",
                "maxlength": 300,
            }
        ),
    )

    class Meta:
        model = Cv
        exclude = ("user",)
        widgets = {
            "skills": forms.CheckboxSelectMultiple(),
        }
