from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is my First Django App</h1>")
def content(request):
    contents = """
        <html>
            <body>
                <center>
                    <h1>Content Page in App</h1>
                </center>
            </body>
        </html>
    """
    return HttpResponse(contents)
def path_request(request):
    path = request.path
    # return HttpResponse(path,content_type='text/html',charset='utf-8')
    scheme = request.scheme
    method = request.method
    path_info = request.path_info
    response = HttpResponse()
    response.headers['Age','Name'] = 20,'Zohaib'
    msg = f"""
        <div style='font-family:sans-serif; background-color:#222; padding:20px; color:#fff; border-radius:5px; width:80%; margin:0 auto;'>
            <p>Path : <b><i>{path}</i></b></p>
            <p>Scheme : <b><i>{scheme}</i></b></p>
            <p>Method : <b><i>{method}</i></b></p>
            <p>Path Info : <b><i>{path_info}</i></b></p>
            <p>Response Headers : <b><i>{response.headers}</i></b></p>
        </div>
    """
    return HttpResponse(msg,content_type='text/html',charset='utf-8')
# def drinks(request,name):
#     query = name
#     return HttpResponse("<h1>%S</h1>"%query)
def menuitems(request,dish):
    items = {
        'Pasta':'Pasta noodles',
        'Falafel':'Deep Friends Patties',
        'Cheesecake':'Cheesecake Foods',
    }
    description = items[dish]
    return HttpResponse(f"<h2>{dish} : {description}</h2>")
# def menuitemsnumber(request,number):
#     items = {
#         1:'Pasta noodles',
#         2:'Deep Friends Patties',
#         3:'Cheesecake Foods',
#     }
#     description = items[number]
#     return HttpResponse(f"<h2>{number} : {description}</h2>")