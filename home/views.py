from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>Hello Word</h1>')
    response.write("This is Home app")
    return response
def home(request):
    return render(request,'/home/template/templates/home/index.html')