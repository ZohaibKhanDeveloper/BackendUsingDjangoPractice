from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Menu
# Create your views here.
def data(request):
    data = f"""
        <div style='background-color:#222; color:white; padding:20px; margin:0 auto; width:30%; font-family:sans-serif;'>
        <center>
        <h1 style='color:lightblue;'>Data inside the Database</h1>
        <table border='1' cellpadding='5' cellspacing='5' style='color:white'>
        <thead>
            <tr style='background-color:#fff; color:#222;'>
                <th>Name</th>
                <th>Cuisine</th>
                <th>price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{Menu.objects.get(pk=1).name} </td>
                <td>{Menu.objects.get(pk=1).cuisine}</td>
                <td>{Menu.objects.get(pk=1).price}</td>
            </tr>
            <tr>
                <td>{Menu.objects.get(pk=2).name} </td>
                <td>{Menu.objects.get(pk=2).cuisine}</td>
                <td>{Menu.objects.get(pk=2).price}</td>
            </tr>
        </tbody>
    </table>
    </center>
        </div> 
    """
    return HttpResponse(data)