from django.shortcuts import render

# Create your views here.
def home(request):
    return render('','home.html')

def about(request):
    return render('','about.html')

def contact(request):
    return render('','contact.html')