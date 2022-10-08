from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("about page") 

def booking(request):
    return HttpResponse("booking page")    

def doctors(request):
    return HttpResponse("doctors page") 

def contact(request):
    return HttpResponse("contact page")          
