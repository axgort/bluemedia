from django.forms import ModelForm
from captcha.fields import CaptchaField

from .models import Error


class ErrorForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Error
        fields = ['details', 'email']
