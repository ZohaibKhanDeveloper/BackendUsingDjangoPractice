from django.shortcuts import render
from formApp.forms import NameForm
from django.http import HttpResponse
# Create your views here.
def formView(request):
    form = NameForm()
    return render(request,'forms.html',{"form":form})