from .models import Logger
from django import forms
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        