from django import forms
from django.forms import fields
from .models import Code


class CodeForm(forms.ModelForm):
    number = forms.CharField(label='code', help_text='Enter your Verification Code')
    class Meta:
        model = Code
        fields = ('number', )