from django.shortcuts import render

# Create your views here.
def home(request):
    details = {
        "name":"Home Page",
        "developer":"Zohaib khan",
        "semester":"BSCS 6th",
        "CGPA":3.67,
    }
    return render(request,'home.html',details)
